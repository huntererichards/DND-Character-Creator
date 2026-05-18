import sys
import os
import tkinter as tk
from tkinter import scrolledtext
from Data import races, classes, backgrounds, alignments, personality_traits, ideals, bonds, flaws
from Character import Character, abilities, FULL_CASTER_SLOTS, HALF_CASTER_SLOTS,WARLOCK_SLOTS,WARLOCK_SLOT_LEVEL
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
from PIL import Image, ImageTk

# --- Utility: Safe resource path for PyInstaller ---
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller bundle"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# --- Character Generation Function ---
def gui_generate_character():
    selected_race = race_var.get() if race_var.get() != "Random" else None
    selected_class = class_var.get() if class_var.get() != "Random" else None
    selected_background = background_var.get() if background_var.get() != "Random" else None
    selected_alignment = alignment_var.get() if alignment_var.get() != "Random" else None
    selected_level = None if level_var.get() == "Random" else int(level_var.get())

    selected_trait = trait_var.get() if trait_var.get() != "Random" else None
    selected_ideal = ideal_var.get() if ideal_var.get() != "Random" else None
    selected_bond = bond_var.get() if bond_var.get() != "Random" else None
    selected_flaw = flaw_var.get() if flaw_var.get() != "Random" else None

    character = Character(
        race_choice=selected_race,
        class_choice=selected_class,
        level=selected_level,
        background=selected_background,
        alignment=selected_alignment,
        trait=selected_trait,
        ideal=selected_ideal,
        bond=selected_bond,
        flaw=selected_flaw
    )

    output_text.delete(1.0, tk.END)
    lines = []
    lines.append(f"===== D&D 5e Character =================================================================")
    lines.append(f"Name: {character.name} ({character.gender})")
    lines.append(f"Race: {character.race} ({character.subrace})")
    lines.append(f"Class: {character.char_class} (Level {character.level})")
    lines.append(f"Hit Points: {character.calculate_hp()}")
    lines.append(f"Background: {character.background}")
    lines.append(f"Alignment: {character.alignment}\n")

    # Stats Table
    lines.append(f"{'Ability':<12}{'Base':>6}   {'Current':>7}")
    lines.append("-" * 30)
    for ability in abilities:
        base = character.base_stats.get(ability, 0)
        current = character.stats.get(ability, 0)
        lines.append(f"{ability:<12}{base:>6}   {current:>7}")
    lines.append("")

    # Equipment
    lines.append("Class Starting Equipment:")
    for item in character.equipment:
        lines.append(f"  - {item}")
    lines.append("\nBackground Equipment:")
    for item in character.background_items:
        lines.append(f"  - {item}")

    # Spell List
    if character.cantrips or character.spells_by_level:
        if character.cantrips:
            lines.append("\nCantrips:")
            for spell in character.cantrips:
                lines.append(f"  - {spell}")

        if character.spells_by_level:


            if character.char_class in ["Bard", "Cleric", "Druid", "Sorcerer", "Wizard"]:
                slot_table = FULL_CASTER_SLOTS
                lines.append("\nSpells by Level:")
                header = f"{'Level':<6} {'Slots':<6} Spells"
                lines.append(header)
                lines.append("-" * 50)
                for lvl in sorted(character.spells_by_level.keys()):
                    num_slots = slot_table.get(character.level, [0] * lvl)[
                        lvl - 1] if character.level in slot_table else 0
                    spells = ", ".join(character.spells_by_level[lvl])
                    lines.append(f"{lvl:<6} {num_slots:<6} {spells}")

            elif character.char_class in ["Paladin", "Ranger"]:
                slot_table = HALF_CASTER_SLOTS
                lines.append("\nSpells by Level:")
                header = f"{'Level':<6} {'Slots':<6} Spells"
                lines.append(header)
                lines.append("-" * 50)
                for lvl in sorted(character.spells_by_level.keys()):
                    num_slots = slot_table.get(character.level, [0] * lvl)[
                        lvl - 1] if character.level in slot_table else 0
                    spells = ", ".join(character.spells_by_level[lvl])
                    lines.append(f"{lvl:<6} {num_slots:<6} {spells}")

            elif character.char_class == "Warlock":
                # Display Warlock spells like other casters, including Mystic Arcanum
                lines.append("\nSpells by Level:")
                header = f"{'Level':<6} {'Slots':<6} Spells"
                lines.append(header)
                lines.append("-" * 50)

                for lvl in sorted(character.spells_by_level.keys()):
                    spells = ", ".join(character.spells_by_level[lvl])
                    # Pact slot level and Mystic Arcanum
                    if lvl == character.warlock_slot_level:
                        slots = character.warlock_slots
                    elif lvl in (6, 7, 8, 9):
                        slots = 1  # Mystic Arcanum
                    else:
                        slots = "—"
                    lines.append(f"{lvl:<6} {slots:<6} {spells}")

            else:
                lines.append("\nThis class does not use spell slots.")

    # Personality
    lines.append("\nPersonality:")
    lines.append(f"  Trait: {character.trait}")
    lines.append(f"  Ideal: {character.ideal}")
    lines.append(f"  Bond: {character.bond}")
    lines.append(f"  Flaw: {character.flaw}")
    lines.append("==========================================================================================")

    output_text.insert(tk.END, "\n".join(lines))


# --- Copy to Clipboard ---
def copy_to_clipboard():
    pyperclip.copy(output_text.get("1.0", tk.END).strip())


# --- Export to PDF ---
def export_to_pdf():
    content = output_text.get("1.0", tk.END).strip()
    if not content:
        return

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "DnD_Character.pdf")
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Monospaced font for alignment
    c.setFont("Courier", 10)
    x_margin = 40
    y = height - 40
    line_height = 14
    max_width = width - 2 * x_margin

    for line in content.split("\n"):
        # Wrap long lines
        if c.stringWidth(line, "Courier", 10) <= max_width:
            c.drawString(x_margin, y, line)
            y -= line_height
        else:
            words = line.split(" ")
            current_line = ""
            for word in words:
                test_line = current_line + ("" if current_line == "" else " ") + word
                if c.stringWidth(test_line, "Courier", 10) <= max_width:
                    current_line = test_line
                else:
                    c.drawString(x_margin, y, current_line)
                    y -= line_height
                    current_line = word
            if current_line:
                c.drawString(x_margin, y, current_line)
                y -= line_height

        # Page break if needed
        if y <= 40:
            c.showPage()
            c.setFont("Courier", 10)
            y = height - 40

    c.save()
    try:
        os.startfile(file_path)
    except AttributeError:
        print(f"PDF saved to: {file_path}")


# --- TKINTER GUI ---
root = ttk.Window(themename="darkly")
root.title("D&D 5e Random Character Generator")
root.state("zoomed")  # full screen

# Set window icon
icon_path = resource_path("icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=1)

# --- Photo ---
image_path = resource_path("dnd.png")
if os.path.exists(image_path):
    img = Image.open(image_path).resize((150, 150))
    photo = ImageTk.PhotoImage(img)
    photo_label = ttk.Label(root, image=photo)
    photo_label.grid(row=0, column=0, sticky="n", padx=5, pady=5)

# --- Frames ---
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=1, sticky="nw")

# Character Frame
char_frame = ttk.LabelFrame(frame, text="Character", padding=10, width=480)
char_frame.grid(row=0, column=0, sticky="nw", padx=5, pady=5)

# Personality Frame
pers_frame = ttk.LabelFrame(frame, text="Personality", padding=10, width=1280)
pers_frame.grid(row=0, column=1, sticky="nw", padx=5, pady=5)

# --- Character Options ---
ttk.Label(char_frame, text="Race:").grid(row=0, column=0, sticky="w")
race_var = tk.StringVar(value="Random")
ttk.Combobox(char_frame, textvariable=race_var, values=["Random"]+list(races.keys()), state="readonly", width=80).grid(row=0, column=1, padx=5, pady=2)

ttk.Label(char_frame, text="Class:").grid(row=1, column=0, sticky="w")
class_var = tk.StringVar(value="Random")
ttk.Combobox(char_frame, textvariable=class_var, values=["Random"]+list(classes.keys()), state="readonly", width=80).grid(row=1, column=1, padx=5, pady=2)

ttk.Label(char_frame, text="Background:").grid(row=2, column=0, sticky="w")
background_var = tk.StringVar(value="Random")
ttk.Combobox(char_frame, textvariable=background_var, values=["Random"]+list(backgrounds.keys()), state="readonly", width=80).grid(row=2, column=1, padx=5, pady=2)

ttk.Label(char_frame, text="Alignment:").grid(row=3, column=0, sticky="w")
alignment_var = tk.StringVar(value="Random")
ttk.Combobox(char_frame, textvariable=alignment_var, values=["Random"]+alignments, state="readonly", width=80).grid(row=3, column=1, padx=5, pady=2)

# --- Personality Options ---
ttk.Label(pers_frame, text="Trait:").grid(row=0, column=0, sticky="w")
trait_var = tk.StringVar(value="Random")
ttk.Combobox(pers_frame, textvariable=trait_var, values=["Random"]+personality_traits, state="readonly", width=100).grid(row=0, column=1, padx=5, pady=2)

ttk.Label(pers_frame, text="Ideal:").grid(row=1, column=0, sticky="w")
ideal_var = tk.StringVar(value="Random")
ttk.Combobox(pers_frame, textvariable=ideal_var, values=["Random"]+ideals, state="readonly", width=100).grid(row=1, column=1, padx=5, pady=2)

ttk.Label(pers_frame, text="Bond:").grid(row=2, column=0, sticky="w")
bond_var = tk.StringVar(value="Random")
ttk.Combobox(pers_frame, textvariable=bond_var, values=["Random"]+bonds, state="readonly", width=100).grid(row=2, column=1, padx=5, pady=2)

ttk.Label(pers_frame, text="Flaw:").grid(row=3, column=0, sticky="w")
flaw_var = tk.StringVar(value="Random")
ttk.Combobox(pers_frame, textvariable=flaw_var, values=["Random"]+flaws, state="readonly", width=100).grid(row=3, column=1, padx=5, pady=2)

# --- Level & Buttons Horizontal Layout ---
button_frame = ttk.Frame(frame)
button_frame.grid(row=2, column=0, columnspan=2, sticky="w", pady=10)

level_label = ttk.Label(button_frame, text="Level:", font=("Arial", 16, "bold"))
level_label.grid(row=0, column=0, sticky="e", padx=(0,5))

level_var = tk.StringVar(value="Random")
level_dropdown = ttk.Combobox(
    button_frame,
    textvariable=level_var,
    values=["Random"] + list(range(1,21)),
    state="readonly",
    width=10,
    font=("Arial", 14)
)
level_dropdown.grid(row=0, column=1, sticky="w", padx=(0,15))

ttk.Button(button_frame, text="Generate Character", command=gui_generate_character, bootstyle="danger").grid(row=0, column=2, padx=5)
ttk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard, bootstyle="danger").grid(row=0, column=3, padx=5)
ttk.Button(button_frame, text="Export to PDF", command=export_to_pdf, bootstyle="danger").grid(row=0, column=4, padx=5)

# --- Output Area ---
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=320, height=35, font=("Consolas", 10))
output_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
