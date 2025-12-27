Modding after long hiatus, had to relearn old things and new stuff to Unreal Engine 4/5.
tools used for mod development

UAsset Diff Tool - Written by Qoqqi
https://github.com/theqoqqi/uasset-diff-tool/

repak Written by truman
https://github.com/trumank/repak

UnrealReZen - Written by NoobInCoding
https://github.com/rm-NoobInCoding/UnrealReZen

FModel
https://fmodel.app/

UAssetGUI - Written by atenfyr
https://github.com/atenfyr/UAssetGUI

UAssetConverter - Written by approved
https://github.com/approved/UnrealUAssetConverter

the mod was inspired by abandoned Red Solstice 2 Redux by ZephyrGlide, kept some values from that and implemented many of my own for "Latest Version"
Checkout his mod
https://www.nexusmods.com/redsolstice2survivors/mods/17

# Red Solstice 2: AHA Rebalanced

**A comprehensive overhaul mod for Red Solstice 2: Survivors.**

This mod aims to revitalize the game by rebalancing weapons, making progression more rewarding, and buffing underused suit modules. It focuses on making higher difficulties approachable through viable strategies rather than grinding, offering powerful upgrades that feel impactful.

Did i made a few things over powered, especially ASV. Hell YA!

## 🛠️ Installation

1.  Download the `.pak` file (e.g., `RS2Redux_P.pak`).
2.  Navigate to your game's installation folder:  
    `\The Red Solstice 2 Survivors\TwinStick\Content\Paks`
3.  Place the `.pak` file inside this folder.
4.  Launch the game.

> **Note:** If playing multiplayer, all players must have the mod installed to prevent desync or crashes.

---

## ⚖️ Changelog

### 🔫 Weapon Rebalancing
Significant adjustments to make every weapon viable.

**Assault Rifles**
* **GAR:**
    * *Auto:* Damage 50 → **60**, RPM 400 → **450**, Crit Chance 10% → **15%**.
    * *Single:* Damage 90 → **125**, Crit Chance 25% → **30%**.
    * *Burst:* Damage 70 → **95**.
* **GAR (Old/Classic):** Damage 55 → **145**, RPM 400 → **175**, Crit Chance 5% → **20%**, Suppression 3 → **8**.
* **High Caliber GAR:** Damage 200 → **255**, Crit Chance 1% → **3%**.
* **HPR Viking (Buffed):**
    * Damage 80 → **250**.
    * RPM 120 → **225**.
    * Range 25m → **35m**.
    * Crit Chance 1% → **25%** (Multiplier **4x**).
    * Suppression 3 → **4**.
* **Strike V Assault (ASV):**
    * *Single:* Damage 400 → **1250**, RPM 200, Range **70m**, Crit 50% (**5.5x**), Suppression 7, Energy Cost **2.5** (Huge buff for sniping).
    * *Burst:* Damage 100 → **150**, RPM **1050**, Range 45m, Crit 40% (**2.5x**), Projectiles per shot **3**.

**Heavy Weapons**
* **LMG:** RPM 500 → **525**.
* **Autocannon:** Auto Damage 110 → **135**, Single Damage 100 → **125**.
* **Minigun:** RPM and Damage tuned for sustained fire.

**Close Quarters (SMG & Shotguns)**
* **SMG:**
    * *Projectiles:* 1 → **2** (Double bullets per shot).
    * *Damage:* 50 → **35** (Net 70 per shot).
    * *RPM:* 600 → **900**.
* **Shotgun (Fast):** Pellets 12 → **14**.
* **Breach Shotgun:** Pellets 4 → **7**.
* **Cerberus:** Damage 100 → **105**, Pellets 20 → **25**.

**Sniper & Precision**
* **Stinger:** Damage 1750 → **1950**, Alt Fire 1000 → **1250**, RPM 30 → **33**.
* **Strike V:** Single Damage 1000 → **1150**.

**Sidearms & Special**
* **Pistol:** Damage 50 → **185**, Suppression 1 → **5**.
* **Smart Gun:**
    * *Auto:* Damage 125 → **175**.
    * *Single:* Damage 50 → **85**, Projectiles 4 → **8**, Energy Cost 10 → **6**.
* **Baton (Melee):** Damage 150 → **575**, Range 250 → **500**, RPM 30 → **60**, Crit Dmg 300% → **400%**.

---

### 🛡️ Suit Modules
Underperforming modules have been tripled or quadrupled in effectiveness.

* **Power Cores:**
    * Small: Energy +15 → **+45**.
    * Medium: Energy +40 → **+120**.
* **Life Support:**
    * Small: HP +30 → **+90**, Regen 0.3 → **0.9**.
    * Medium: HP +90 → **+270**, Regen 1.0 → **3.0**.
* **Overcharge:**
    * Start Skills +1 → **+4**.
    * Max Level +1 → **+4**.
    * Energy Penalty: -10% → **-1%** (Penalty reduced significantly).
* **Capacitor:** Suit Energy +10 → **+25**.
* **Agility (Medium):** Movement Speed +6% → **+30%**.
* **Primary Extender:** Primary Slots +1 → **+3**.
* **Enhancer:** Skill Damage +7% → **+40%**.
* **Stabilizer System:** Final & Initial Spread **-45%** (Huge accuracy boost).
* **Overwatch Upgrade:**
    * Range Bonus: 1.25x → **45m** flat increase.
    * Retarget Time: -20% → **-60%** (Faster switching).
    * Manual Aim Time: -20% → **-60%**.

---

### 💊 Buffs & Consumables
Durations have been extended to make consumables less tedious.

* **Medical:**
    * **Medkit:** 30s → **45s**.
    * **Fibrin Bandage:** 2s → **3s**.
    * **Stimulants:** 8s → **15s**.
    * **Antivenom:** 60s → **80s**.
* **Combat:**
    * **Energy Battery:** 60s → **360s** (Lasts 6 minutes now!).
    * **Focus Fire:** 5s → **30s**.
    * **Armor Overload:** 12s → **25s**.
    * **Suit Energized:** 20s → **25s**.

---

### 🎖️ Player Progression (Ranks)
A complete overhaul of the leveling curve. Every rank feels rewarding.

* **Standard Ranks (2-24):** Progressive buffs to **Max Health**, **Max Energy**, and **Suit Power**, totaling a **42%** increase at max level.
* **Capstone Ranks:**
    * **Rank 5:** Overwatch Range **x10**, Spread **-15%**, Suppression **+2**.
    * **Rank 10:** Skill Cooldown **-5%** (Stacking), Skill Damage **x5**, Activation Range **x5**.
    * **Rank 15:** Item Damage **x15**, Skill Radius **x10**, Ailment Resistance **15%**.
    * **Rank 20:** Skill Duration **x20**, Starting Skill Points **+2**, Skill Cost **-10%**.
    * **Rank 25:**
        * Overwatch Range **x10**.
        * Skill Cooldown **-5%** (Stacking).
        * Skill Radius **x10**.
        * Skill Duration **x15**.
        * Critical Damage **+50%**.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
