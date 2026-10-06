"""
Задание 5 (Вариант 4): График y = x^0.5.

Рисуем первую четверть графика (x ≥ 0, y ≥ 0).
Высота минимум 9 строк.
"""

import math


def draw_graph(width=40, height=12, x_max=16, y_max=4):
    """
    Рисует график y = √x.

    Параметры:
        width  — ширина в символах (ось X)
        height — высота в строках (ось Y), минимум 9
        x_max  — максимальное значение x
        y_max  — максимальное значение y
    """
    # Проверяем, что высота не меньше 9
    if height < 9:
        height = 9

    # === 1. Создаём пустую сетку ===
    # grid[r][c] — символ в строке r, столбце c
    grid = []
    for r in range(height + 1):
        row = [" "] * (width + 1)
        grid.append(row)

    # === 2. Отмечаем точки графика ===
    for col in range(width + 1):
        # Вычисляем x по столбцу
        x = x_max * col / width
        # Вычисляем y = √x
        y = math.sqrt(x)

        # Пропускаем точки выше графика
        if y > y_max:
            continue

        # Переводим y в строку (снизу вверх → сверху вниз)
        row = height - int(y / y_max * height)

        # Ставим звёздочку
        if 0 <= row <= height:
            grid[row][col] = "*"

    # === 3. Рисуем оси ===
    # Ось Y (нулевой столбец)
    for r in range(height + 1):
        if grid[r][0] == " ":
            grid[r][0] = "|"

    # Ось X (последняя строка)
    for c in range(width + 1):
        if grid[height][c] == " ":
            grid[height][c] = "-"

    # Начало координат
    grid[height][0] = "+"

    # === 4. Печатаем ===
    print(f"\nГрафик y = x^0.5  (x ∈ [0, {x_max}], y ∈ [0, {y_max}])")
    print("  ^ y")
    for r in range(height + 1):
        print("  |" + "".join(grid[r]))
    print("  +" + "-" * (width + 1) + "> x")


if __name__ == "__main__":
    draw_graph()