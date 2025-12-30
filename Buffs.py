import json
import copy

# --- Configuration ---
input_file = 'BuffData_DT.json'
mod_file = 'BuffData_DT(mod).json'
output_file = 'BuffData_DT(modified).json'

print(f"Reading files...")
try:
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        original_data = json.load(f)
    with open(mod_file, 'r', encoding='utf-8-sig') as f:
        mod_data = json.load(f)
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

# --- Helper Functions ---
def find_prop(props, name):
    for p in props:
        if p.get('Name') == name:
            return p
    return None

def get_row_map(data):
    if 'Exports' in data and len(data['Exports']) > 0:
        return {r['Name']: r for r in data['Exports'][0]['Table']['Data']}
    return {}

def get_row(data, row_name):
    rows = data['Exports'][0]['Table']['Data']
    for row in rows:
        if row['Name'] == row_name:
            return row
    return None

def update_modifier(struct_list, attr_name, new_val, mod_type="EModifierType::EMT_StackingMultiply"):
    found = False
    for entry in struct_list:
        val_props = entry['Value']
        aff_attr = find_prop(val_props, 'AffectedAttribute')
        if aff_attr and aff_attr.get('Value') == attr_name:
            mod_map = find_prop(val_props, 'Modifiers')
            if mod_map and mod_map['Value']:
                pair = mod_map['Value'][0]
                pair[1]['Value'] = float(new_val)
                if mod_type:
                    pair[0]['Value'] = mod_type
            found = True
            break
    
    if not found and len(struct_list) > 0:
        template = copy.deepcopy(struct_list[0])
        t_props = template['Value']
        find_prop(t_props, 'AffectedAttribute')['Value'] = attr_name
        mod_map = find_prop(t_props, 'Modifiers')
        if mod_map and mod_map['Value']:
            pair = mod_map['Value'][0]
            pair[0]['Value'] = mod_type
            pair[1]['Value'] = float(new_val)
        struct_list.append(template)

# --- Step 1: Patch NameMap ---
original_namemap = set(original_data.get('NameMap', []))
mod_namemap = mod_data.get('NameMap', [])
for name in mod_namemap:
    if name not in original_namemap:
        original_data['NameMap'].append(name)
        original_namemap.add(name)
custom_names = [
    "EAttribute::EA_OverwatchRange", "EAttribute::EA_OverwatchRetargeting", 
    "EAttribute::EA_LongAimInterval", "EModifierType::EMT_Add", 
    "EModifierType::EMT_StackingMultiply", "EAttribute::EWA_SpreadMaximum",
    "EAttribute::EWA_SpreadMinimum"
]
for name in custom_names:
    if name not in original_namemap:
        original_data['NameMap'].append(name)
        original_namemap.add(name)

# --- Step 2: Apply Mod Durations (Safe Bulk Update) ---
orig_rows = original_data['Exports'][0]['Table']['Data']
mod_row_map = get_row_map(mod_data)
safe_properties = ["Duration", "Period", "MaxStacks", "Priority", "bIsStackable"]

for row in orig_rows:
    name = row['Name']
    if "Discipline" in name: continue 

    if name in mod_row_map:
        mod_row = mod_row_map[name]
        for prop_name in safe_properties:
            p_orig = find_prop(row['Value'], prop_name)
            p_mod = find_prop(mod_row['Value'], prop_name)
            if p_orig and p_mod:
                if p_orig.get('Value') != p_mod.get('Value'):
                    p_orig['Value'] = p_mod.get('Value')

        p_attr_orig = find_prop(row['Value'], "AttributeModifiers")
        p_attr_mod = find_prop(mod_row['Value'], "AttributeModifiers")
        if p_attr_mod and str(p_attr_orig) != str(p_attr_mod):
             if not p_attr_orig:
                 row['Value'].append(copy.deepcopy(p_attr_mod))
             else:
                 p_attr_orig['Value'] = copy.deepcopy(p_attr_mod['Value'])

# --- Step 3: Custom Buffs ---

# Overwatch Upgrade (Fixed Range & Times)
ow_buff = get_row(original_data, 'OverwatchUpgrade')
if ow_buff:
    stack_prop = find_prop(ow_buff['Value'], 'StackableAttributeModifiers')
    if stack_prop:
        mod_list = stack_prop['Value']
        update_modifier(mod_list, "EAttribute::EA_OverwatchRange", 3000.0, "EModifierType::EMT_Add")
        update_modifier(mod_list, "EAttribute::EA_OverwatchRetargeting", -60.0, "EModifierType::EMT_StackingMultiply")
        update_modifier(mod_list, "EAttribute::EA_LongAimInterval", -60.0, "EModifierType::EMT_StackingMultiply")
        print("Updated OverwatchUpgrade")

# Stabilizer System (-45% Spread)
stab_buff = get_row(original_data, 'StabilizerSystem')
if stab_buff:
    # Check both Fixed and Stackable
    mod_prop = find_prop(stab_buff['Value'], 'FixedAttributeModifiers')
    if not mod_prop: mod_prop = find_prop(stab_buff['Value'], 'StackableAttributeModifiers')
    
    if mod_prop:
        mod_list = mod_prop['Value']
        # Create template from Overwatch if list is empty
        template = None
        if len(mod_list) > 0:
            template = copy.deepcopy(mod_list[0])
        elif ow_buff and stack_prop and len(stack_prop['Value']) > 0:
            template = copy.deepcopy(stack_prop['Value'][0])
        
        if template:
            mod_list.clear()
            # Final Spread -45%
            m1 = copy.deepcopy(template)
            find_prop(m1['Value'], 'AffectedAttribute')['Value'] = "EAttribute::EWA_SpreadMaximum"
            pair = find_prop(m1['Value'], 'Modifiers')['Value'][0]
            pair[0]['Value'] = "EModifierType::EMT_StackingMultiply"
            pair[1]['Value'] = -150.0
            mod_list.append(m1)
            # Initial Spread -45%
            m2 = copy.deepcopy(template)
            find_prop(m2['Value'], 'AffectedAttribute')['Value'] = "EAttribute::EWA_SpreadMinimum"
            pair = find_prop(m2['Value'], 'Modifiers')['Value'][0]
            pair[0]['Value'] = "EModifierType::EMT_StackingMultiply"
            pair[1]['Value'] = -150.0
            mod_list.append(m2)
            print("Updated StabilizerSystem Buff")

# --- Step 4: Save ---
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(original_data, f, indent=2)
print(f"Saved {output_file}")