import tkinter as tk
import random
import pygame


# Лабораторная работа №3
# Вариант 4. Генератор ключей


# Задание 3. Реализация генератора ключей

# Определение весового коэффициента символа
def get_weight(char):
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return ord(char) - ord("A") + 1  # A=1, B=2, ...
    elif char in "0123456789":
        return int(char)
    else:
        return None


# Вычисление суммы весов символов блока
def calculate_weight(block):
    total = 0

    for char in block:
        weight = get_weight(char)
        total += weight  # Cong don trong so

    return total


# Генерация блока из четырёх символов
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


# Генерация ключа из трёх блоков
def generate_key():
    block1 = generate_block()
    block2 = generate_block()
    block3 = generate_block()

    key = f"{block1}-{block2}-{block3}"

    return key


# Отображение сгенерированного ключа
def show_key():
    key = generate_key()

    entry_key.delete(0, tk.END)
    entry_key.insert(0, key)


# Дополнительное задание. Музыка и анимация

# Анимация заголовка
def animate_title():
    if lbl_title.cget("fg") == "white":
        lbl_title.config(fg="yellow")
    else:
        lbl_title.config(fg="white")

    root.after(500, animate_title)


# Остановка музыки при закрытии окна
def on_close():
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    root.destroy()



if __name__ == "__main__":

    root = tk.Tk()
    root.title("Game Key Generator")

    # Фоновая музыка
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    root.protocol("WM_DELETE_WINDOW", on_close)

    # Задание 1. Выбор игры и фонового изображения

    # Загрузка фонового изображения
    bg_image = tk.PhotoImage(file="background.png").subsample(2, 2)

    # Размер окна
    root.geometry(f"{bg_image.width()}x{bg_image.height()}")

    bg_label = tk.Label(root, image=bg_image, bd=0)
    bg_label.grid(row=0, column=0, sticky="nsew")

    # Задание 2. Создание графического интерфейса

    # Настройка сетки главного окна
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Настройка сетки фонового изображения
    bg_label.columnconfigure(0, weight=1)
    bg_label.rowconfigure(0, weight=1)
    bg_label.rowconfigure(4, weight=1)

    # Заголовок программы
    lbl_title = tk.Label(
        bg_label,
        text="GAME KEY GENERATOR",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="black"
    )
    lbl_title.grid(row=1, column=0, pady=15)

    # Поле для отображения ключа
    entry_key = tk.Entry(
        bg_label,
        font=("Arial", 16),
        width=25,
        justify="center"
    )
    entry_key.grid(row=2, column=0, pady=15)

    # Кнопка генерации ключа
    btn_generate = tk.Button(
        bg_label,
        text="GENERATE KEY",
        font=("Arial", 14),
        command=show_key
    )
    btn_generate.grid(row=3, column=0, pady=15)

    # Запуск анимации
    animate_title()

    # Запуск главного цикла программы
    root.mainloop()
