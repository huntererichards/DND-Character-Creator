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
"""
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
"""
classes = {
    "Bard": {
        "priority": ["Charisma", "Dexterity", "Constitution"],
        "equipment": ["Rapier", "Lute", "Leather Armor", "Dagger", "Entertainer's Pack"],
        "spellcasting": True,
        "cantrips": [
            "Blade Ward", "Dancing Lights", "Friends", "Light", "Mage Hand",
            "Mending", "Message", "Minor Illusion", "Prestidigitation", "Thunderclap",
            "True Strike", "Vicious Mockery"
        ],
        "level1": [
            "Animal Friendship", "Bane", "Charm Person", "Comprehend Languages",
            "Cure Wounds", "Detect Magic", "Disguise Self", "Dissonant Whispers",
            "Faerie Fire", "Feather Fall", "Healing Word", "Heroism",
            "Identify", "Illusory Script", "Longstrider", "Silent Image",
            "Sleep", "Speak with Animals", "Tasha's Hideous Laughter", "Thunderwave",
            "Unseen Servant"
        ],
        "level2": [
            "Animal Messenger", "Blindness/Deafness", "Calm Emotions", "Cloud of Daggers",
            "Crown of Madness", "Detect Thoughts", "Enhance Ability", "Enthrall",
            "Heat Metal", "Hold Person", "Invisibility", "Knock", "Lesser Restoration",
            "Locate Animals or Plants", "Locate Object", "Magic Mouth",
            "Phantasmal Force", "See Invisibility", "Shatter", "Silence",
            "Skywrite", "Suggestion", "Warding Wind", "Zone of Truth"
        ],
        "level3": [
            "Bestow Curse", "Clairvoyance", "Dispel Magic", "Fear", "Feign Death",
            "Glyph of Warding", "Hypnotic Pattern", "Leomund's Tiny Hut",
            "Major Image", "Nondetection", "Plant Growth", "Sending",
            "Speak with Dead", "Speak with Plants", "Stinking Cloud",
            "Tiny Servant", "Tongues"
        ],
        "level4": [
            "Compulsion", "Confusion", "Dimension Door", "Greater Invisibility",
            "Hallucinatory Terrain", "Locate Creature", "Phantasmal Killer",
            "Polymorph"
        ],
        "level5": [
            "Animate Objects", "Awaken", "Dominate Person", "Dream", "Geas",
            "Greater Restoration", "Hold Monster", "Legend Lore",
            "Mass Cure Wounds", "Mislead", "Modify Memory", "Planar Binding",
            "Raise Dead", "Scrying", "Seeming", "Teleportation Circle"
        ],
        "level6": [
            "Eyebite", "Find the Path", "Guards and Wards", "Mass Suggestion",
            "Otto's Irresistible Dance", "Programmed Illusion", "True Seeing"
        ],
        "level7": [
            "Etherealness", "Forcecage", "Mirage Arcane", "Mordenkainen's Magnificent Mansion",
            "Mordenkainen's Sword", "Project Image", "Regenerate", "Resurrection",
            "Symbol", "Teleport"
        ],
        "level8": [
            "Dominate Monster", "Feeblemind", "Glibness", "Mind Blank",
            "Power Word Stun"
        ],
        "level9": [
            "Foresight", "Power Word Heal", "Power Word Kill", "True Polymorph"
        ]
    },

    "Cleric": {
        "priority": ["Wisdom", "Constitution", "Strength"],
        "equipment": ["Mace", "Scale Mail", "Shield", "Holy Symbol"],
        "spellcasting": True,
        "cantrips": [
            "Guidance", "Light", "Mending", "Resistance", "Sacred Flame",
            "Spare the Dying", "Thaumaturgy", "Toll the Dead", "Word of Radiance"
        ],
        "level1": [
            "Bane", "Bless", "Ceremony", "Command", "Create or Destroy Water",
            "Cure Wounds", "Detect Evil and Good", "Detect Magic",
            "Detect Poison and Disease", "Guiding Bolt", "Healing Word",
            "Inflict Wounds", "Protection from Evil and Good", "Purify Food and Drink",
            "Sanctuary", "Shield of Faith"
        ],
        "level2": [
            "Aid", "Augury", "Blindness/Deafness", "Calm Emotions", "Continual Flame",
            "Enhance Ability", "Find Traps", "Gentle Repose", "Hold Person",
            "Lesser Restoration", "Locate Object", "Prayer of Healing",
            "Protection from Poison", "Silence", "Spiritual Weapon", "Warding Bond",
            "Zone of Truth"
        ],
        "level3": [
            "Animate Dead", "Beacon of Hope", "Bestow Curse", "Clairvoyance",
            "Create Food and Water", "Daylight", "Dispel Magic", "Feign Death",
            "Glyph of Warding", "Magic Circle", "Mass Healing Word",
            "Meld into Stone", "Protection from Energy", "Remove Curse",
            "Revivify", "Sending", "Speak with Dead", "Spirit Guardians",
            "Tongues", "Water Walk"
        ],
        "level4": [
            "Banishment", "Control Water", "Death Ward", "Divination",
            "Freedom of Movement", "Guardian of Faith", "Locate Creature",
            "Stone Shape"
        ],
        "level5": [
            "Commune", "Contagion", "Dispel Evil and Good", "Flame Strike",
            "Geas", "Greater Restoration", "Hallow", "Insect Plague",
            "Legend Lore", "Mass Cure Wounds", "Planar Binding",
            "Raise Dead", "Scrying"
        ],
        "level6": [
            "Blade Barrier", "Create Undead", "Find the Path",
            "Forbiddance", "Harm", "Heal", "Heroes' Feast",
            "Planar Ally", "True Seeing", "Word of Recall"
        ],
        "level7": [
            "Conjure Celestial", "Divine Word", "Etherealness",
            "Fire Storm", "Plane Shift", "Regenerate",
            "Resurrection", "Symbol"
        ],
        "level8": [
            "Antimagic Field", "Control Weather", "Earthquake",
            "Holy Aura"
        ],
        "level9": [
            "Astral Projection", "Gate", "Mass Heal", "True Resurrection"
        ]
    },

    "Druid": {
        "priority": ["Wisdom", "Constitution", "Dexterity"],
        "equipment": ["Wooden Shield", "Scimitar", "Leather Armor", "Druidic Focus", "Explorer's Pack"],
        "spellcasting": True,
        "cantrips": [
            "Control Flames", "Create Bonfire", "Druidcraft", "Frostbite", "Guidance",
            "Gust", "Infestation", "Magic Stone", "Mending", "Mold Earth", "Poison Spray",
            "Primal Savagery", "Produce Flame", "Resistance", "Shape Water", "Shillelagh",
            "Thorn Whip"
        ],
        "level1": [
            "Absorb Elements", "Animal Friendship", "Charm Person", "Create or Destroy Water",
            "Cure Wounds", "Detect Magic", "Detect Poison and Disease", "Entangle", "Faerie Fire",
            "Fog Cloud", "Goodberry", "Healing Word", "Ice Knife", "Jump", "Longstrider",
            "Purify Food and Drink", "Snare", "Speak with Animals", "Thunderwave"
        ],
        "level2": [
            "Animal Messenger", "Barkskin", "Beast Sense", "Darkvision", "Dust Devil",
            "Earthbind", "Enhance Ability", "Find Traps", "Flame Blade", "Flaming Sphere",
            "Gust of Wind", "Healing Spirit", "Heat Metal", "Hold Person", "Lesser Restoration",
            "Locate Animals or Plants", "Locate Object", "Moonbeam", "Pass without Trace",
            "Protection from Poison", "Skywrite", "Spike Growth", "Warding Wind"
        ],
        "level3": [
            "Call Lightning", "Conjure Animals", "Daylight", "Dispel Magic",
            "Erupting Earth", "Feign Death", "Meld into Stone", "Plant Growth",
            "Protection from Energy", "Sleet Storm", "Speak with Plants",
            "Tidal Wave", "Wall of Water", "Water Breathing", "Water Walk",
            "Wind Wall"
        ],
        "level4": [
            "Blight", "Confusion", "Conjure Minor Elementals", "Conjure Woodland Beings",
            "Control Water", "Dominate Beast", "Elemental Bane", "Freedom of Movement",
            "Giant Insect", "Grasping Vine", "Hallucinatory Terrain", "Ice Storm",
            "Locate Creature", "Polymorph", "Stone Shape", "Stoneskin",
            "Wall of Fire"
        ],
        "level5": [
            "Antilife Shell", "Awaken", "Commune with Nature", "Conjure Elemental",
            "Contagion", "Geas", "Greater Restoration", "Insect Plague", "Maelstrom",
            "Mass Cure Wounds", "Planar Binding", "Reincarnate", "Scrying",
            "Tree Stride", "Wall of Stone", "Wrath of Nature"
        ],
        "level6": [
            "Conjure Fey", "Find the Path", "Heal", "Heroes' Feast", "Move Earth",
            "Sunbeam", "Transport via Plants", "Wall of Thorns"
        ],
        "level7": [
            "Fire Storm", "Mirage Arcane", "Plane Shift", "Regenerate",
            "Reverse Gravity", "Resurrection", "Symbol", "Teleport"
        ],
        "level8": [
            "Animal Shapes", "Antimagic Field", "Control Weather", "Earthquake",
            "Sunburst"
        ],
        "level9": [
            "Foresight", "Shapechange", "Storm of Vengeance", "True Resurrection"
        ]
    },

    "Paladin": {
        "priority": ["Strength", "Charisma", "Constitution"],
        "equipment": ["Longsword", "Shield", "Chain Mail", "Holy Symbol", "Javelins"],
        "spellcasting": True,
        "cantrips": [],
        "level1": [
            "Bless", "Command", "Compelled Duel", "Cure Wounds", "Detect Magic",
            "Divine Favor", "Heroism", "Protection from Evil and Good", "Searing Smite",
            "Shield of Faith", "Thunderous Smite", "Wrathful Smite"
        ],
        "level2": [
            "Aid", "Branding Smite", "Find Steed", "Lesser Restoration",
            "Magic Weapon", "Protection from Poison", "Spiritual Weapon"
        ],
        "level3": [
            "Aura of Vitality", "Blinding Smite", "Create Food and Water",
            "Crusader's Mantle", "Daylight", "Dispel Magic", "Elemental Weapon",
            "Magic Circle", "Remove Curse", "Revivify"
        ],
        "level4": [
            "Aura of Life", "Aura of Purity", "Banishing Smite", "Death Ward",
            "Staggering Smite"
        ],
        "level5": [
            "Circle of Power", "Destructive Smite", "Geas", "Hold Monster",
            "Raise Dead"
        ]
    },

    "Ranger": {
        "priority": ["Dexterity", "Wisdom", "Constitution"],
        "equipment": ["Longbow", "Two Shortswords", "Leather Armor", "Explorer's Pack"],
        "spellcasting": True,
        "cantrips": [],
        "level1": [
            "Alarm", "Animal Friendship", "Cure Wounds", "Detect Magic",
            "Detect Poison and Disease", "Ensnaring Strike", "Fog Cloud",
            "Goodberry", "Hail of Thorns", "Hunter's Mark", "Jump",
            "Longstrider", "Speak with Animals"
        ],
        "level2": [
            "Animal Messenger", "Barkskin", "Darkvision", "Find Traps",
            "Lesser Restoration", "Locate Animals or Plants", "Pass without Trace",
            "Spike Growth"
        ],
        "level3": [
            "Conjure Animals", "Lightning Arrow", "Nondetection", "Plant Growth",
            "Protection from Energy", "Speak with Plants", "Water Breathing",
            "Water Walk"
        ],
        "level4": [
            "Conjure Woodland Beings", "Freedom of Movement", "Grasping Vine",
            "Locate Creature", "Stoneskin"
        ],
        "level5": [
            "Commune with Nature", "Conjure Volley", "Swift Quiver", "Tree Stride"
        ]
    },

    "Sorcerer": {
        "priority": ["Charisma", "Constitution", "Dexterity"],
        "equipment": ["Dagger", "Light Crossbow", "Component Pouch", "Explorer's Pack"],
        "spellcasting": True,
        "cantrips": [
            "Acid Splash", "Blade Ward", "Chill Touch", "Dancing Lights", "Fire Bolt",
            "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion",
            "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp",
            "True Strike"
        ],
        "level1": [
            "Burning Hands", "Charm Person", "Chromatic Orb", "Color Spray",
            "Comprehend Languages", "Detect Magic", "Disguise Self", "Expeditious Retreat",
            "False Life", "Feather Fall", "Find Familiar", "Fog Cloud", "Jump",
            "Mage Armor", "Magic Missile", "Shield", "Silent Image", "Sleep",
            "Thunderwave", "Witch Bolt"
        ],
        "level2": [
            "Alter Self", "Arcane Lock", "Blur", "Darkness", "Darkvision", "Detect Thoughts",
            "Enlarge/Reduce", "Flaming Sphere", "Gust of Wind", "Hold Person", "Invisibility",
            "Knock", "Levitate", "Mirror Image", "Misty Step", "Scorching Ray", "See Invisibility",
            "Shatter", "Spider Climb", "Suggestion", "Web"
        ],
        "level3": [
            "Counterspell", "Dispel Magic", "Fear", "Fireball", "Fly", "Gaseous Form",
            "Haste", "Hypnotic Pattern", "Lightning Bolt", "Major Image", "Nondetection",
            "Phantom Steed", "Protection from Energy", "Remove Curse", "Sending",
            "Sleet Storm", "Slow", "Stinking Cloud", "Tongues", "Water Breathing",
            "Water Walk"
        ],
        "level4": [
            "Arcane Eye", "Banishment", "Blight", "Confusion", "Control Water", "Dimension Door",
            "Greater Invisibility", "Ice Storm", "Phantasmal Killer", "Polymorph", "Stone Shape",
            "Stoneskin", "Wall of Fire"
        ],
        "level5": [
            "Animate Objects", "Bigby’s Hand", "Cloudkill", "Cone of Cold",
            "Conjure Elemental", "Contact Other Plane", "Creation", "Dominate Person",
            "Dream", "Geas", "Hold Monster", "Legend Lore", "Mislead", "Modify Memory",
            "Passwall", "Planar Binding", "Scrying", "Seeming", "Telekinesis",
            "Teleportation Circle", "Wall of Force", "Wall of Stone"
        ],
        "level6": [
            "Arcane Gate", "Chain Lightning", "Circle of Death", "Conjure Fey",
            "Contingency", "Create Undead", "Disintegrate", "Drawmij’s Instant Summons",
            "Eyebite", "Flesh to Stone", "Globe of Invulnerability", "Guards and Wards",
            "Mass Suggestion", "Move Earth", "Otiluke’s Freezing Sphere",
            "Programmed Illusion", "Sunbeam", "True Seeing", "Wall of Ice"
        ],
        "level7": [
            "Delayed Blast Fireball", "Etherealness", "Finger of Death", "Fire Storm",
            "Forcecage", "Mirage Arcane", "Mordenkainen’s Magnificent Mansion",
            "Mordenkainen’s Sword", "Plane Shift", "Prismatic Spray", "Project Image",
            "Reverse Gravity", "Sequester", "Simulacrum", "Symbol", "Teleport"
        ],
        "level8": [
            "Antimagic Field", "Antipathy/Sympathy", "Clone", "Control Weather",
            "Demiplane", "Dominate Monster", "Earthquake", "Feeblemind", "Incendiary Cloud",
            "Maze", "Mind Blank", "Power Word Stun"
        ],
        "level9": [
            "Astral Projection", "Foresight", "Gate", "Imprisonment", "Mass Polymorph",
            "Meteor Swarm", "Power Word Kill", "Prismatic Wall", "Shapechange",
            "Time Stop", "True Polymorph", "Wish"
        ]
    },

    "Warlock": {
        "priority": ["Charisma", "Constitution", "Dexterity"],
        "equipment": ["Light Crossbow", "Simple Weapon", "Component Pouch", "Dagger", "Leather Armor"],
        "spellcasting": True,
        "cantrips": [
            "Blade Ward", "Chill Touch", "Eldritch Blast", "Friends", "Mage Hand",
            "Minor Illusion", "Poison Spray", "Prestidigitation", "True Strike"
        ],
        "level1": [
            "Armor of Agathys", "Arms of Hadar", "Charm Person", "Comprehend Languages",
            "Expeditious Retreat", "Hellish Rebuke", "Hex", "Illusory Script",
            "Protection from Evil and Good", "Unseen Servant", "Witch Bolt"
        ],
        "level2": [
            "Cloud of Daggers", "Crown of Madness", "Darkness", "Detect Thoughts",
            "Enthrall", "Hold Person", "Invisibility", "Mirror Image", "Misty Step",
            "Phantasmal Force", "Ray of Enfeeblement", "Shatter", "Spider Climb",
            "Suggestion"
        ],
        "level3": [
            "Counterspell", "Dispel Magic", "Fear", "Fly", "Gaseous Form", "Hunger of Hadar",
            "Hypnotic Pattern", "Magic Circle", "Major Image", "Remove Curse",
            "Tongues", "Vampiric Touch"
        ],
        "level4": [
            "Banishment", "Blight", "Dimension Door", "Hallucinatory Terrain",
            "Phantasmal Killer", "Greater Invisibility"
        ],
        "level5": [
            "Animate Dead", "Cloudkill", "Contact Other Plane", "Danse Macabre",
            "Dream", "Hold Monster", "Scrying", "Wall of Force"
        ],
        "level6": [
            "Circle of Death", "Conjure Fey", "Create Undead", "Eyebite", "Mass Suggestion"
        ],
        "level7": [
            "Finger of Death", "Forcecage", "Plane Shift", "Power Word Pain"
        ],
        "level8": [
            "Demiplane", "Dominate Monster", "Feeblemind", "Glibness", "Mind Blank"
        ],
        "level9": [
            "Astral Projection", "Foresight", "Imprisonment", "Power Word Kill", "True Polymorph"
        ]
    },

    "Wizard": {
        "priority": ["Intelligence", "Constitution", "Dexterity"],
        "equipment": ["Spellbook", "Quarterstaff", "Component pouch", "Dagger"],
        "spellcasting": True,
        "cantrips": [
            "Acid Splash", "Blade Ward", "Chill Touch", "Dancing Lights",
            "Fire Bolt", "Friends", "Light", "Mage Hand", "Mending",
            "Message", "Minor Illusion", "Poison Spray", "Prestidigitation",
            "Ray of Frost", "Shocking Grasp", "True Strike"
        ],
        "level1": [
            "Alarm", "Burning Hands", "Charm Person", "Chromatic Orb",
            "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self",
            "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar",
            "Fog Cloud", "Grease", "Identify", "Illusory Script", "Jump",
            "Mage Armor", "Magic Missile", "Protection from Evil and Good",
            "Ray of Sickness", "Shield", "Silent Image", "Sleep", "Tasha’s Hideous Laughter",
            "Tenser’s Floating Disk", "Thunderwave", "Unseen Servant", "Witch Bolt"
        ],
        "level2": [
            "Alter Self", "Arcane Lock", "Blindness/Deafness", "Blur",
            "Cloud of Daggers", "Continual Flame", "Crown of Madness", "Darkness",
            "Detect Thoughts", "Enlarge/Reduce", "Flaming Sphere", "Gust of Wind",
            "Hold Person", "Invisibility", "Knock", "Levitate", "Mirror Image",
            "Misty Step", "Phantasmal Force", "Scorching Ray", "See Invisibility",
            "Shatter", "Spider Climb", "Suggestion", "Web"
        ],
        "level3": [
            "Animate Dead", "Bestow Curse", "Blink", "Counterspell", "Dispel Magic",
            "Fear", "Fireball", "Fly", "Gaseous Form", "Haste", "Hypnotic Pattern",
            "Leomund’s Tiny Hut", "Lightning Bolt", "Magic Circle", "Major Image",
            "Nondetection", "Phantom Steed", "Protection from Energy", "Remove Curse",
            "Sending", "Sleet Storm", "Slow", "Stinking Cloud", "Tongues", "Water Breathing",
            "Water Walk"
        ],
        "level4": [
            "Arcane Eye", "Banishment", "Blight", "Confusion", "Control Water",
            "Dimension Door", "Evard’s Black Tentacles", "Fabricate", "Fire Shield",
            "Greater Invisibility", "Ice Storm", "Leomund’s Secret Chest", "Locate Creature",
            "Mordenkainen’s Faithful Hound", "Mordenkainen’s Private Sanctum",
            "Otiluke’s Resilient Sphere", "Phantasmal Killer", "Polymorph", "Stone Shape",
            "Stoneskin", "Wall of Fire"
        ],
        "level5": [
            "Animate Objects", "Bigby’s Hand", "Cloudkill", "Cone of Cold",
            "Conjure Elemental", "Contact Other Plane", "Creation", "Dispel Evil and Good",
            "Dominate Person", "Dream", "Geas", "Hold Monster", "Legend Lore",
            "Mislead", "Modify Memory", "Passwall", "Planar Binding", "Rary’s Telepathic Bond",
            "Scrying", "Seeming", "Telekinesis", "Teleportation Circle", "Wall of Force",
            "Wall of Stone"
        ],
        "level6": [
            "Arcane Gate", "Chain Lightning", "Circle of Death", "Conjure Fey",
            "Contingency", "Create Undead", "Disintegrate", "Drawmij’s Instant Summons",
            "Eyebite", "Flesh to Stone", "Globe of Invulnerability", "Guards and Wards",
            "Mass Suggestion", "Move Earth", "Otiluke’s Freezing Sphere", "Programmed Illusion",
            "Sunbeam", "True Seeing", "Wall of Ice"
        ],
        "level7": [
            "Delayed Blast Fireball", "Etherealness", "Finger of Death", "Fire Storm",
            "Forcecage", "Mirage Arcane", "Mordenkainen’s Magnificent Mansion", "Mordenkainen’s Sword",
            "Plane Shift", "Prismatic Spray", "Project Image", "Reverse Gravity", "Sequester",
            "Simulacrum", "Symbol", "Teleport"
        ],
        "level8": [
            "Antimagic Field", "Antipathy/Sympathy", "Clone", "Control Weather",
            "Demiplane", "Dominate Monster", "Earthquake", "Feeblemind", "Incendiary Cloud",
            "Maze", "Mind Blank", "Power Word Stun"
        ],
        "level9": [
            "Astral Projection", "Foresight", "Gate", "Imprisonment", "Mass Polymorph",
            "Meteor Swarm", "Power Word Kill", "Prismatic Wall", "Shapechange", "Time Stop",
            "True Polymorph", "Wish"
        ]
            },

    "Rogue": {"priority": ["Dexterity", "Intelligence", "Charisma"],
        "equipment": ["Rapier", "Shortbow", "20 arrows", "Leather armor", "Dagger (2)", "Thieves’ tools", "Burglar’s pack"],
        "spellcasting": False},
 "Fighter": {"priority": ["Strength", "Constitution", "Dexterity"],
        "equipment": ["Chain mail", "Longsword", "Shield", "Crossbow", "20 bolts", "Dungeoneer’s pack"],
        "spellcasting": False},
    "Monk": {"priority": ["Dexterity", "Wisdom", "Constitution"],
        "equipment": ["Shortsword", "Dart (10)", "Explorer’s pack"], "spellcasting": False},
    "Barbarian": {"priority": ["Strength", "Constitution", "Dexterity"],
        "equipment": ["Greataxe", "Handaxe (2)", "Explorer’s pack"], "spellcasting": False},


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