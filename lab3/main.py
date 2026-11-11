import tkinter as tk
import random
import pygame

# Task 3: Generator

# Tinh trong so cua mot ky tu
def get_weight(char):
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return ord(char) - ord("A") + 1
    elif char in "0123456789":
        return int(char)
    else:
        return None


# Tinh tong trong so cua mot block
def calculate_weight(block):
    total = 0

    for char in block:
        weight = get_weight(char)
        total += weight

    return total


# Tao mot block gom 4 ky tu
def generate_block():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    while True:
        block = ""

        for i in range(4):
            char = random.choice(characters)
            block += char

        total = calculate_weight(block)

        if 30 <= total <= 35:
            return block


# Tao key gom 3 block
def generate_key():
    block1 = generate_block()
    block2 = generate_block()
    block3 = generate_block()

    key = f"{block1}-{block2}-{block3}"

    return key


# Hien thi key trong Entry
def show_key():
    key = generate_key()

    entry_key.delete(0, tk.END)
    entry_key.insert(0, key)

def animate_title():
    if lbl_title.cget("fg") == "white":
        lbl_title.config(fg="yellow")
    else:
        lbl_title.config(fg="white")

    root.after(500, animate_title)


root = tk.Tk()
root.title("Game Key Generator")


# Background music
pygame.mixer.init()                 # khoi tao pygame mixer
pygame.mixer.music.load("music.mp3") #doc file nhac
pygame.mixer.music.set_volume(0.3) # dat am luong
pygame.mixer.music.play(-1)         # phat nhac lap lai vo han

def on_close():
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# Task 1 + Task 2: GUI
# Hinh nen
bg_image = tk.PhotoImage(file="background.png").subsample(2, 2)  # Thu nho anh neu kich thuoc qua lon

# Cho cua so co kich thuoc bang anh
root.geometry(f"{bg_image.width()}x{bg_image.height()}")

# Tao Label chua anh nen
bg_label = tk.Label(root, image=bg_image, bd=0)
bg_label.grid(row=0, column=0, sticky="nsew")

# Cho phep root mo rong
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Cau hinh grid ben trong bg_label
bg_label.columnconfigure(0, weight=1)
bg_label.rowconfigure(0, weight=1)
bg_label.rowconfigure(4, weight=1)

# Title
lbl_title = tk.Label(
    bg_label,
    text="GAME KEY GENERATOR",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="black"
)
lbl_title.grid(row=1, column=0, pady=15)

# Key
entry_key = tk.Entry(
    bg_label,
    font=("Arial", 16),
    width=25,
    justify="center"
)
entry_key.grid(row=2, column=0, pady=15)

# Button
btn_generate = tk.Button(
    bg_label,
    text="GENERATE KEY",
    font=("Arial", 14),
    command=show_key
)
btn_generate.grid(row=3, column=0, pady=15)

for i in range(10):
    key = generate_key()
    blocks = key.split("-")

    print("Key:", key)

    for block in blocks:
        total = calculate_weight(block)
        print(block, total)

        assert 30 <= total <= 35

    print("-------------")

animate_title()
root.mainloop()
