"""
Lab 1 — главный файл.

Запускает все 5 заданий по очереди:
    1. Флаг Польши
    2. Узор d
    3. Анимация (ёлка)
    4. Диаграмма %
    5. График y = √x
"""

import sys
from pathlib import Path

# Разрешаем импорт из папки src/
sys.path.insert(0, str(Path(__file__).parent))

# Импортируем все задания
from src import task1_flag
from src import task2_pattern
from src import task3_animation
from src import task4_diagram
from src import task5_graph


# === Задание 1: Флаг Польши ===
print("=" * 50)
print("ЗАДАНИЕ 1: ФЛАГ ПОЛЬШИ")
print("=" * 50)
task1_flag.draw_flag()
input("\n[Enter] чтобы продолжить...")


# === Задание 2: Узор d ===
print("\n" + "=" * 50)
print("ЗАДАНИЕ 2: УЗОР d")
print("=" * 50)
task2_pattern.draw_pattern()
input("\n[Enter] чтобы продолжить...")


# === Задание 3: Анимация ===
print("\n" + "=" * 50)
print("ЗАДАНИЕ 3: АНИМАЦИЯ (ЁЛКА)")
print("=" * 50)
task3_animation.animate()
input("\n[Enter] чтобы продолжить...")


# === Задание 4: Диаграмма ===
print("\n" + "=" * 50)
print("ЗАДАНИЕ 4: ДИАГРАММА %")
print("=" * 50)
task4_diagram.main()
input("\n[Enter] чтобы продолжить...")


# === Задание 5: График ===
print("\n" + "=" * 50)
print("ЗАДАНИЕ 5: ГРАФИК y = √x")
print("=" * 50)
task5_graph.draw_graph()
input("\n[Enter] чтобы закончить...")

print("\n Все задания выполнены!")
