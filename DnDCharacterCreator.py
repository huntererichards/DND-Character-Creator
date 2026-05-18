"""
import random

# --- Alignments ---
alignments = [
    "Lawful Good", "Neutral Good", "Chaotic Good",
    "Lawful Neutral", "True Neutral", "Chaotic Neutral",
    "Lawful Evil", "Neutral Evil", "Chaotic Evil"
]

# --- Personality traits, ideals, bonds, flaws ---
personality_traits = [
    "I always have a plan for what to do when things go wrong.",
    "I idolize a particular hero and measure my deeds against theirs.",
    "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
    "I speak in a booming, dramatic voice.",
    "I ask a lot of questions, sometimes too many."
]

ideals = [
    "Respect. All people deserve to be treated with dignity.",
    "Charity. I always help those in need, no matter the cost.",
    "Freedom. Chains are meant to be broken, as are those who forge them.",
    "Knowledge. The path to power and self-improvement is through knowledge.",
    "Glory. I must earn glory in battle, for myself and my clan."
]

bonds = [
    "I would die to recover an ancient artifact of my faith.",
    "I will face any challenge to win the approval of my family.",
    "I seek to protect those who cannot protect themselves.",
    "Someone I loved died because of a mistake I made. I will never repeat it.",
    "My honor is my life."
]

flaws = [
    "I judge others harshly, and myself even more severely.",
    "I am inflexible in my thinking.",
    "Once I pick a goal, I become obsessed with it to the detriment of everything else.",
    "I enjoy the thrill of taking risks.",
    "I will never fully trust anyone other than myself."
]

races = {
    "Human": {
        "subraces": ["Standard", "Variant"],
        "bonuses": {
            "Standard": {"Strength": 1, "Dexterity": 1, "Constitution": 1,
                         "Intelligence": 1, "Wisdom": 1, "Charisma": 1},
            "Variant": {}  # Choose later (skipped for simplicity)
        }
    },
    "Elf": {
        "subraces": ["High Elf", "Wood Elf", "Drow"],
        "bonuses": {
            "High Elf": {"Dexterity": 2, "Intelligence": 1},
            "Wood Elf": {"Dexterity": 2, "Wisdom": 1},
            "Drow": {"Dexterity": 2, "Charisma": 1}
        }
    },
    "Dwarf": {
        "subraces": ["Hill Dwarf", "Mountain Dwarf"],
        "bonuses": {
            "Hill Dwarf": {"Constitution": 2, "Wisdom": 1},
            "Mountain Dwarf": {"Constitution": 2, "Strength": 2}
        }
    },
    "Halfling": {
        "subraces": ["Lightfoot", "Stout"],
        "bonuses": {
            "Lightfoot": {"Dexterity": 2, "Charisma": 1},
            "Stout": {"Dexterity": 2, "Constitution": 1}
        }
    },
    "Dragonborn": {
        "subraces": ["Standard"],
        "bonuses": {"Standard": {"Strength": 2, "Charisma": 1}}
    },
    "Gnome": {
        "subraces": ["Forest Gnome", "Rock Gnome"],
        "bonuses": {
            "Forest Gnome": {"Intelligence": 2, "Dexterity": 1},
            "Rock Gnome": {"Intelligence": 2, "Constitution": 1}
        }
    },
    "Half-Elf": {
        "subraces": ["Standard"],
        "bonuses": {"Standard": {"Charisma": 2, "Dexterity": 1, "Constitution": 1}}
    },
    "Half-Orc": {
        "subraces": ["Standard"],
        "bonuses": {"Standard": {"Strength": 2, "Constitution": 1}}
    },
    "Tiefling": {
        "subraces": ["Standard"],
        "bonuses": {"Standard": {"Charisma": 2, "Intelligence": 1}}
    }
}

# --- Classes (priority, gear, spellcasting) ---
classes = {
    "Barbarian": {"priority": ["Strength", "Constitution", "Dexterity"],
        "equipment": ["Greataxe", "Handaxe (2)", "Explorer’s pack"], "spellcasting": False},
    "Bard": {"priority": ["Charisma", "Dexterity", "Constitution"],
        "equipment": ["Rapier", "Lute", "Leather armor", "Dagger", "Entertainer’s pack"],
        "spellcasting": True,
        "cantrips": ["Vicious Mockery", "Prestidigitation", "Mage Hand", "Minor Illusion"],
        "level1": ["Healing Word", "Charm Person", "Thunderwave", "Cure Wounds", "Disguise Self"]},
    "Cleric": {"priority": ["Wisdom", "Constitution", "Strength"],
        "equipment": ["Mace", "Shield", "Scale mail", "Holy symbol", "Priest’s pack"],
        "spellcasting": True,
        "cantrips": ["Guidance", "Sacred Flame", "Thaumaturgy", "Light"],
        "level1": ["Cure Wounds", "Bless", "Shield of Faith", "Detect Magic", "Inflict Wounds"]},
    "Druid": {"priority": ["Wisdom", "Constitution", "Dexterity"],
        "equipment": ["Wooden shield", "Scimitar", "Leather armor", "Herbalism kit", "Explorer’s pack"],
        "spellcasting": True,
        "cantrips": ["Druidcraft", "Produce Flame", "Shillelagh", "Guidance"],
        "level1": ["Entangle", "Cure Wounds", "Faerie Fire", "Goodberry", "Thunderwave"]},
    "Fighter": {"priority": ["Strength", "Constitution", "Dexterity"],
        "equipment": ["Chain mail", "Longsword", "Shield", "Crossbow", "20 bolts", "Dungeoneer’s pack"],
        "spellcasting": False},
    "Monk": {"priority": ["Dexterity", "Wisdom", "Constitution"],
        "equipment": ["Shortsword", "Dart (10)", "Explorer’s pack"], "spellcasting": False},
    "Paladin": {"priority": ["Strength", "Charisma", "Constitution"],
        "equipment": ["Chain mail", "Longsword", "Shield", "Holy symbol", "Priest’s pack"],
        "spellcasting": True,
        "cantrips": [],
        "level1": ["Divine Favor", "Shield of Faith", "Cure Wounds", "Command", "Compelled Duel"]},
    "Ranger": {"priority": ["Dexterity", "Wisdom", "Constitution"],
        "equipment": ["Scale mail", "Longbow", "20 arrows", "Shortswords (2)", "Explorer’s pack"],
        "spellcasting": True,
        "cantrips": [],
        "level1": ["Hunter’s Mark", "Cure Wounds", "Hail of Thorns", "Detect Magic", "Speak with Animals"]},
    "Rogue": {"priority": ["Dexterity", "Intelligence", "Charisma"],
        "equipment": ["Rapier", "Shortbow", "20 arrows", "Leather armor", "Dagger (2)", "Thieves’ tools", "Burglar’s pack"],
        "spellcasting": False},
    "Sorcerer": {"priority": ["Charisma", "Constitution", "Dexterity"],
        "equipment": ["Dagger", "Component pouch", "Light crossbow", "20 bolts", "Explorer’s pack"],
        "spellcasting": True,
        "cantrips": ["Fire Bolt", "Ray of Frost", "Prestidigitation", "Mage Hand", "Acid Splash"],
        "level1": ["Magic Missile", "Shield", "Chromatic Orb", "Burning Hands", "Mage Armor"]},
    "Warlock": {"priority": ["Charisma", "Constitution", "Dexterity"],
        "equipment": ["Light crossbow", "20 bolts", "Dagger (2)", "Component pouch", "Scholar’s pack"],
        "spellcasting": True,
        "cantrips": ["Eldritch Blast", "Mage Hand", "Minor Illusion", "Prestidigitation"],
        "level1": ["Hex", "Armor of Agathys", "Witch Bolt", "Charm Person", "Hellish Rebuke"]},
    "Wizard": {"priority": ["Intelligence", "Constitution", "Dexterity"],
        "equipment": ["Spellbook", "Quarterstaff", "Component pouch", "Scholar’s pack"],
        "spellcasting": True,
        "cantrips": ["Fire Bolt", "Mage Hand", "Light", "Ray of Frost", "Prestidigitation"],
        "level1": ["Magic Missile", "Mage Armor", "Shield", "Sleep", "Detect Magic"]}
}

# Background gear
backgrounds = {
    "Acolyte": ["Holy symbol", "Prayer book", "5 sticks of incense"],
    "Charlatan": ["Disguise kit", "Forgery kit", "Fine clothes"],
    "Criminal": ["Crowbar", "Dark clothes", "Thieves' tools"],
    "Entertainer": ["Musical instrument", "Costume", "Favor from an admirer"],
    "Folk Hero": ["Artisan's tools", "Shovel", "Iron pot"],
    "Guild Artisan": ["Artisan’s tools", "Letter of introduction", "Traveler’s clothes"],
    "Hermit": ["Scroll case", "Winter blanket", "Herbalism kit"],
    "Noble": ["Fine clothes", "Signet ring", "Scroll of pedigree"],
    "Outlander": ["Hunting trap", "Animal trophy", "Traveler’s clothes"],
    "Sage": ["Bottle of ink", "Quill", "Small knife"],
    "Sailor": ["Belaying pin", "Rope (50ft)", "Lucky charm"],
    "Soldier": ["Insignia of rank", "Trophy from fallen enemy", "Dice set"],
    "Urchin": ["Small knife", "Map of the city", "Pet mouse"]
}

abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

# --- Expanded Race Name Pools ---
names = {
    "Human": {
        "male": [
            "Alaric", "Baldric", "Cedric", "Darian", "Edric", "Garrick", "Roland", "Tobias",
            "Marcus", "Julian", "Victor", "Samuel", "Leopold", "Henry", "Thomas", "William"
        ],
        "female": [
            "Elena", "Kara", "Isolde", "Marian", "Selene", "Talia", "Yvette",
            "Cassandra", "Amelia", "Diana", "Rosalind", "Evelyn", "Joanna", "Lydia", "Sophia"
        ]
    },
    "Elf": {
        "male": [
            "Aerith", "Caelthas", "Eryndor", "Faelar", "Theren", "Varis", "Altharion",
            "Erevan", "Legolas", "Elrohir", "Celeborn", "Rhovan", "Aelar", "Galinndan"
        ],
        "female": [
            "Arwen", "Luthien", "Sylvara", "Elira", "Naivara", "Shalana", "Enna",
            "Keyleth", "Alleria", "Meriele", "Tiriel", "Anastrianna", "Shava", "Ilyana"
        ]
    },
    "Dwarf": {
        "male": [
            "Baern", "Dain", "Thorin", "Gimli", "Brom", "Rurik", "Bruenor",
            "Harbek", "Morgran", "Orsik", "Travok", "Vondal", "Barendd", "Delg"
        ],
        "female": [
            "Dis", "Helja", "Vistra", "Hlin", "Gurdis", "Kathra", "Eldeth",
            "Kristryd", "Sannl", "Torbera", "Diesa", "Falkrunn", "Ilde", "Mardred"
        ]
    },
    "Halfling": {
        "male": [
            "Alton", "Cade", "Milo", "Perrin", "Roscoe", "Wellby",
            "Finnan", "Garret", "Osborn", "Merric", "Corrin", "Lyle"
        ],
        "female": [
            "Bree", "Cora", "Lavinia", "Merla", "Seraphina", "Verna",
            "Andry", "Callie", "Jillian", "Kithri", "Lidda", "Portia"
        ]
    },
    "Dragonborn": {
        "male": [
            "Arjhan", "Balasar", "Donaar", "Ghesh", "Kriv", "Rhogar",
            "Torinn", "Medrash", "Nadarr", "Pandjed", "Shamash", "Tarhun"
        ],
        "female": [
            "Akra", "Daar", "Harann", "Mishann", "Sora", "Thava",
            "Uadjit", "Vezera", "Nala", "Khagra", "Zhera", "Perra"
        ]
    },
    "Tiefling": {
        "male": [
            "Akmenos", "Damakos", "Leucis", "Mordai", "Therai", "Zerxes",
            "Kairon", "Morthos", "Skamos", "Vexar", "Zeriel", "Kaspar"
        ],
        "female": [
            "Akta", "Criella", "Kallista", "Makaria", "Phelaia", "Rieta",
            "Furla", "Anakis", "Zhera", "Orianna", "Lilith", "Zephyra"
        ]
    },
    "Gnome": {
        "male": [
            "Alston", "Boddynock", "Fonkin", "Wrenn", "Zook", "Bimp",
            "Jebeddo", "Namfoodle", "Orryn", "Seebo", "Trig", "Nackle"
        ],
        "female": [
            "Bimpnottin", "Caramip", "Loopmottin", "Nissa", "Tana",
            "Donella", "Ellyjobell", "Oda", "Roywyn", "Shamil", "Vanya"
        ]
    },
    "Half-Orc": {
        "male": [
            "Dench", "Feng", "Gell", "Henk", "Thokk", "Urgosh",
            "Ront", "Krusk", "Skar", "Mog", "Drogan", "Brug"
        ],
        "female": [
            "Baggi", "Engong", "Myev", "Ovak", "Yevelda", "Shautha",
            "Kansif", "Emen", "Volen", "Nella", "Ruzza", "Vorla"
        ]
    }
}

# fallback if race missing
default_names = {
    "male": ["Aric", "Baldric", "Dain", "Theron"],
    "female": ["Lyra", "Mira", "Selene", "Tessa"]
}


# --- Stat Rolling ---
def roll_stat():
    rolls = [random.randint(1,6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

# --- Character Generator ---
def generate_character():
    # Race + subrace
    race = random.choice(list(races.keys()))
    subrace = random.choice(races[race]["subraces"])
    bonuses = races[race]["bonuses"][subrace]

    # Gender + Name
    gender = random.choice(["male", "female"])
    if race in names:
        name = random.choice(names[race][gender])
    else:
        name = random.choice(default_names[gender])

    # Class + background
    char_class = random.choice(list(classes.keys()))
    background = random.choice(list(backgrounds.keys()))

    # Roll stats
    rolled_stats = sorted([roll_stat() for _ in range(6)], reverse=True)
    priorities = classes[char_class]["priority"]
    stats = {a: 0 for a in abilities}

    for i, ability in enumerate(priorities):
        stats[ability] = rolled_stats[i]

    leftover = [a for a in abilities if stats[a] == 0]
    for i, ability in enumerate(leftover):
        stats[ability] = rolled_stats[len(priorities) + i]

    # Apply racial bonuses
    for ability, bonus in bonuses.items():
        stats[ability] += bonus

    # Alignment + personality
    alignment = random.choice(alignments)
    trait = random.choice(personality_traits)
    ideal = random.choice(ideals)
    bond = random.choice(bonds)
    flaw = random.choice(flaws)

    # --- Output ---
    print("===== Random D&D 5e Character =====")
    print(f"Name: {name} ({gender})")
    print(f"Race: {race} ({subrace})")
    print(f"Class: {char_class}")
    print(f"Background: {background}")
    print(f"Alignment: {alignment}")

    print("\nAbility Scores (with racial bonuses):")
    for ability, score in stats.items():
        print(f"  {ability}: {score}")

    print("\nClass Starting Equipment:")
    for item in classes[char_class]["equipment"]:
        print(f"  - {item}")

    print("\nBackground Equipment:")
    for item in backgrounds[background]:
        print(f"  - {item}")

    if classes[char_class]["spellcasting"]:
        print("\nSpells Known:")
        cantrips = random.sample(classes[char_class]["cantrips"], min(2, len(classes[char_class]["cantrips"])))
        level1 = random.sample(classes[char_class]["level1"], min(2, len(classes[char_class]["level1"])))
        if cantrips:
            print("  Cantrips:")
            for spell in cantrips:
                print(f"    - {spell}")
        if level1:
            print("  1st-level Spells:")
            for spell in level1:
                print(f"    - {spell}")

    print("\nPersonality:")
    print(f"  Trait: {trait}")
    print(f"  Ideal: {ideal}")
    print(f"  Bond: {bond}")
    print(f"  Flaw: {flaw}")

    print("==================================")

# Run
#if __name__ == "__main__":
 #   generate_character()

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# --- GUI Generation Wrapper ---
def gui_generate_character():
    selected_race = race_var.get()
    selected_class = class_var.get()

    # Race
    if selected_race == "Random":
        race = random.choice(list(races.keys()))
    else:
        race = selected_race

    subrace = random.choice(races[race]["subraces"])
    bonuses = races[race]["bonuses"][subrace]

    # Gender + Name
    gender = random.choice(["male", "female"])
    if race in names:
        name = random.choice(names[race][gender])
    else:
        name = random.choice(default_names[gender])

    # Class
    if selected_class == "Random":
        char_class = random.choice(list(classes.keys()))
    else:
        char_class = selected_class

    # Background
    background = random.choice(list(backgrounds.keys()))

    # Stats
    rolled_stats = sorted([roll_stat() for _ in range(6)], reverse=True)
    priorities = classes[char_class]["priority"]
    stats = {a: 0 for a in abilities}

    for i, ability in enumerate(priorities):
        stats[ability] = rolled_stats[i]

    leftover = [a for a in abilities if stats[a] == 0]
    for i, ability in enumerate(leftover):
        stats[ability] = rolled_stats[len(priorities) + i]

    for ability, bonus in bonuses.items():
        stats[ability] += bonus

    # Alignment and traits
    alignment = random.choice(alignments)
    trait = random.choice(personality_traits)
    ideal = random.choice(ideals)
    bond = random.choice(bonds)
    flaw = random.choice(flaws)

    # --- Output to Text Box ---
    output = []
    output.append("===== Random D&D 5e Character =====")
    output.append(f"Name: {name} ({gender})")
    output.append(f"Race: {race} ({subrace})")
    output.append(f"Class: {char_class}")
    output.append(f"Background: {background}")
    output.append(f"Alignment: {alignment}")

    output.append("\nAbility Scores (with racial bonuses):")
    for ability, score in stats.items():
        output.append(f"  {ability}: {score}")

    output.append("\nClass Starting Equipment:")
    for item in classes[char_class]["equipment"]:
        output.append(f"  - {item}")

    output.append("\nBackground Equipment:")
    for item in backgrounds[background]:
        output.append(f"  - {item}")

    if classes[char_class]["spellcasting"]:
        cantrips = random.sample(classes[char_class]["cantrips"], min(2, len(classes[char_class]["cantrips"])))
        level1 = random.sample(classes[char_class]["level1"], min(2, len(classes[char_class]["level1"])))
        if cantrips:
            output.append("\n  Cantrips:")
            for spell in cantrips:
                output.append(f"    - {spell}")
        if level1:
            output.append("  1st-level Spells:")
            for spell in level1:
                output.append(f"    - {spell}")

    output.append("\nPersonality:")
    output.append(f"  Trait: {trait}")
    output.append(f"  Ideal: {ideal}")
    output.append(f"  Bond: {bond}")
    output.append(f"  Flaw: {flaw}")
    output.append("==================================")

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "\n".join(output))


# --- TKINTER GUI ---
root = tk.Tk()
root.title("D&D 5e Random Character Generator")

# Dropdowns
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="ew")

ttk.Label(frame, text="Select Race:").grid(row=0, column=0, sticky="w")
race_var = tk.StringVar(value="Random")
race_options = ["Random"] + list(races.keys())
race_menu = ttk.Combobox(frame, textvariable=race_var, values=race_options, state="readonly")
race_menu.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Select Class:").grid(row=1, column=0, sticky="w")
class_var = tk.StringVar(value="Random")
class_options = ["Random"] + list(classes.keys())
class_menu = ttk.Combobox(frame, textvariable=class_var, values=class_options, state="readonly")
class_menu.grid(row=1, column=1, padx=5, pady=5)

# Button
generate_button = ttk.Button(frame, text="Generate Random Character", command=gui_generate_character)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Output Box
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30, font=("Consolas", 10))
output_text.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()

"""