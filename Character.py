import random
from Data import races, names, default_names, classes, backgrounds, abilities, alignments, personality_traits, ideals, bonds, flaws
from Utils import roll_stat

# --- Spell Slot Tables ---
FULL_CASTER_SLOTS = {
    1: [2,0,0,0,0,0,0,0,0],
    2: [3,0,0,0,0,0,0,0,0],
    3: [4,2,0,0,0,0,0,0,0],
    4: [4,3,0,0,0,0,0,0,0],
    5: [4,3,2,0,0,0,0,0,0],
    6: [4,3,3,0,0,0,0,0,0],
    7: [4,3,3,1,0,0,0,0,0],
    8: [4,3,3,2,0,0,0,0,0],
    9: [4,3,3,3,1,0,0,0,0],
    10:[4,3,3,3,2,0,0,0,0],
    11:[4,3,3,3,2,1,0,0,0],
    12:[4,3,3,3,2,1,0,0,0],
    13:[4,3,3,3,2,1,1,0,0],
    14:[4,3,3,3,2,1,1,0,0],
    15:[4,3,3,3,2,1,1,1,0],
    16:[4,3,3,3,2,1,1,1,0],
    17:[4,3,3,3,2,1,1,1,1],
    18:[4,3,3,3,3,1,1,1,1],
    19:[4,3,3,3,3,2,1,1,1],
    20:[4,3,3,3,3,2,2,1,1],
}

WARLOCK_SLOTS = {
    1: [1],
    2: [2],
    3: [2],
    4: [2],
    5: [2],
    6: [2],
    7: [2],
    8: [2],
    9: [2],
    10: [2],
    11: [3],
    12: [3],
    13: [3],
    14: [3],
    15: [3],
    16: [3],
    17: [4],
    18: [4],
    19: [4],
    20: [4],
}

WARLOCK_SLOT_LEVEL = {
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    9: 5,
    10: 5,
    11: 5,
    12: 5,
    13: 5,
    14: 5,
    15: 5,
    16: 5,
    17: 5,
    18: 5,
    19: 5,
    20: 5,
}

HALF_CASTER_SLOTS = {
    1: [0,0,0,0,0],
    2: [2,0,0,0,0],
    3: [3,0,0,0,0],
    4: [3,0,0,0,0],
    5: [4,2,0,0,0],
    6: [4,2,0,0,0],
    7: [4,3,0,0,0],
    8: [4,3,0,0,0],
    9: [4,3,2,0,0],
    10:[4,3,2,0,0],
    11:[4,3,3,0,0],
    12:[4,3,3,0,0],
    13:[4,3,3,1,0],
    14:[4,3,3,1,0],
    15:[4,3,3,2,0],
    16:[4,3,3,2,0],
    17:[4,3,3,3,1],
    18:[4,3,3,3,1],
    19:[4,3,3,3,2],
    20:[4,3,3,3,2],
}

# --- Cantrips by Class & Level ---
CANTRIPS_BY_CLASS_LEVEL = {
    "Wizard":  {1: 3, 4: 4, 10: 5, 20: 5},
    "Sorcerer":{1: 4, 4: 5, 10: 5, 20: 5},
    "Warlock": {1: 2, 4: 3, 10: 4, 16: 5},
    "Cleric":  {1: 3, 4: 4, 10: 5, 14: 6, 20: 6},
    "Druid":   {1: 2, 4: 3, 10: 4, 14: 5, 20: 5},
    "Bard":    {1: 2, 4: 3, 10: 4, 14: 5, 20: 5},
    "Paladin": {1: 0},
    "Ranger":  {1: 0}
}

# --- Character Class ---
class Character:
    def __init__(self, race_choice=None, class_choice=None, level=None, background=None, alignment=None,
                 trait=None, ideal=None, bond=None, flaw=None):
        # --- Race & Subrace ---
        self.race = race_choice if race_choice else random.choice(list(races.keys()))
        self.subrace = random.choice(races[self.race]["subraces"])
        self.bonuses = races[self.race]["bonuses"][self.subrace]

        # --- Gender & Name ---
        self.gender = random.choice(["male", "female"])
        self.name = self.choose_name()

        # --- Class & Level ---
        self.char_class = class_choice if class_choice else random.choice(list(classes.keys()))
        self.level = int(level) if level is not None else random.randint(1, 20)

        # --- Background & Stats ---
        self.background = background if background else random.choice(list(backgrounds.keys()))
        self.base_stats = self.generate_base_stats()
        self.stats = self.scale_stats_by_level()
        self.background_items = backgrounds[self.background]

        # --- Personality ---
        self.alignment = alignment if alignment else random.choice(alignments)
        self.trait = trait if trait else random.choice(personality_traits)
        self.ideal = ideal if ideal else random.choice(ideals)
        self.bond = bond if bond else random.choice(bonds)
        self.flaw = flaw if flaw else random.choice(flaws)

        # --- Equipment ---
        self.equipment = classes[self.char_class]["equipment"]

        # --- Spellcasting ---
        self.cantrips = []
        self.spells_by_level = {}
        if classes[self.char_class]["spellcasting"]:
            self.generate_spells()

        if self.char_class == "Warlock":
            self.warlock_slots = WARLOCK_SLOTS.get(self.level, [0])[0]
            self.warlock_slot_level = WARLOCK_SLOT_LEVEL.get(self.level, 1)
        else:
            self.warlock_slots = 0
            self.warlock_slot_level = 0

    # --- Helpers ---
    def choose_name(self):
        if self.race in names:
            return random.choice(names[self.race][self.gender])
        return random.choice(default_names[self.gender])

    # --- Stats ---
    def generate_base_stats(self):
        rolled_stats = sorted([roll_stat() for _ in range(6)], reverse=True)
        priorities = classes[self.char_class]["priority"]
        stats = {a: 0 for a in abilities}

        # Assign primary stats first
        for i, ability in enumerate(priorities):
            stats[ability] = rolled_stats[i]

        # Assign remaining stats
        leftover = [a for a in abilities if stats[a] == 0]
        for i, ability in enumerate(leftover):
            stats[ability] = rolled_stats[len(priorities) + i]

        # Add racial bonuses
        for ability, bonus in self.bonuses.items():
            stats[ability] += bonus

        return stats

    def scale_stats_by_level(self):
        stats = self.base_stats.copy()
        priorities = classes[self.char_class]["priority"]
        primary = priorities[0]
        secondary = priorities[1] if len(priorities) > 1 else None

        milestones = [4, 8, 12, 16, 19]
        for milestone in milestones:
            if self.level >= milestone:
                points = 2
                if stats[primary] < 20:
                    inc = min(points, 20 - stats[primary])
                    stats[primary] += inc
                    points -= inc
                if secondary and points > 0 and stats[secondary] < 20:
                    inc = min(points, 20 - stats[secondary])
                    stats[secondary] += inc
                    points -= inc
                if points > 0:
                    remaining_stats = [a for a in abilities if stats[a] < 20]
                    while points > 0 and remaining_stats:
                        stat_choice = random.choice(remaining_stats)
                        stats[stat_choice] += 1
                        points -= 1
                        if stats[stat_choice] >= 20:
                            remaining_stats.remove(stat_choice)
        return stats

    # --- HP Calculation ---
    def calculate_hp(self):
        HIT_DICE = {
            "Barbarian": 12,
            "Fighter": 10,
            "Paladin": 10,
            "Ranger": 10,
            "Bard": 8,
            "Cleric": 8,
            "Druid": 8,
            "Monk": 8,
            "Rogue": 8,
            "Warlock": 8,
            "Sorcerer": 6,
            "Wizard": 6
        }

        hit_die = HIT_DICE[self.char_class]
        con_mod = (self.stats["Constitution"] - 10) // 2

        # Level 1: max hit die + CON
        hp = hit_die + con_mod

        # Levels 2+: average hit die + CON per level
        if self.level > 1:
            avg_gain = ((hit_die // 2) + 1) + con_mod
            hp += (self.level - 1) * avg_gain

        return max(hp, 1)  # ensure minimum 1 HP

    # --- Spell Generation ---
    def generate_spells(self):
        if self.char_class in ["Bard", "Cleric", "Druid", "Sorcerer", "Wizard","Warlock"]:
            slot_table = FULL_CASTER_SLOTS
            max_level = 9
        elif self.char_class in ["Paladin", "Ranger"]:
            slot_table = HALF_CASTER_SLOTS
            max_level = 5
        else:
            return

        # --- Determine number of cantrips per class & level ---
        if self.char_class in CANTRIPS_BY_CLASS_LEVEL:
            levels = sorted(CANTRIPS_BY_CLASS_LEVEL[self.char_class].keys())
            num_cantrips = 0
            for lvl in levels:
                if self.level >= lvl:
                    num_cantrips = CANTRIPS_BY_CLASS_LEVEL[self.char_class][lvl]
            available_cantrips = classes[self.char_class].get("cantrips", [])
            self.cantrips = random.sample(available_cantrips, min(num_cantrips, len(available_cantrips)))

        # --- Generate leveled spells ---
        slots = slot_table[self.level]
        for lvl in range(1, max_level + 1):
            num_slots = slots[lvl - 1]
            if num_slots > 0:
                available_spells = classes[self.char_class].get(f"level{lvl}", [])
                if available_spells:
                    self.spells_by_level[lvl] = random.sample(available_spells, min(num_slots, len(available_spells)))

    # --- Formatting Output ---
    def format_output(self):
        lines = []
        lines.append("===== Random D&D 5e Character =====")
        lines.append(f"Name: {self.name} ({self.gender})")
        lines.append(f"Race: {self.race} ({self.subrace})")
        lines.append(f"Class: {self.char_class} (Level {self.level})")
        lines.append(f"Background: {self.background}")
        lines.append(f"Alignment: {self.alignment}")

        lines.append("\nAbility Scores (Base / Current):")
        for ability in abilities:
            base = self.base_stats[ability]
            current = self.stats[ability]
            lines.append(f"  {ability}: {base} / {current}")

        # --- HP Display ---
        lines.append(f"\nHit Points: {self.calculate_hp()}")

        lines.append("\nClass Starting Equipment:")
        for item in self.equipment:
            lines.append(f"  - {item}")

        lines.append("\nBackground Equipment:")
        for item in self.background_items:
            lines.append(f"  - {item}")

        if self.cantrips or self.spells_by_level:
            if self.cantrips:
                lines.append("\nCantrips:")
                for spell in self.cantrips:
                    lines.append(f"  - {spell}")
            for lvl in sorted(self.spells_by_level.keys()):
                spells = self.spells_by_level[lvl]
                lines.append(f"{self.ordinal(lvl)}-level Spells:")
                for spell in spells:
                    lines.append(f"  - {spell}")

        lines.append("\nPersonality:")
        lines.append(f"  Trait: {self.trait}")
        lines.append(f"  Ideal: {self.ideal}")
        lines.append(f"  Bond: {self.bond}")
        lines.append(f"  Flaw: {self.flaw}")
        lines.append("==================================")
        return "\n".join(lines)

    @staticmethod
    def ordinal(n):
        if 10 <= n % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
        return f"{n}{suffix}"
