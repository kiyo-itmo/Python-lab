# Лабораторная работа №4 - Дополнительные задания
# Variant 4

from itertools import combinations
from main import items, MAX_CELLS, gen_table_memo, find_selected, calculate_score


# Допзадание 1 - Инвентарь на 7 ячеек

def check_7_cells():

    max_cells = 7

    #Создаём таблицу динамического программирования
    dp_table = gen_table_memo(items, max_cells)

    #Находим оптимальный набор предметов
    selected_items = find_selected(dp_table, items, max_cells)

    #Вычисляем итоговые очки выживания
    final_score = calculate_score(selected_items)

    #Получаем максимальные очки выбранных предметов
    max_points = dp_table[-1][-1]

    print("Допзадание 1 - Инвентарь на 7 ячеек")
    print("Выбранные предметы:", selected_items)
    print("Максимальные очки предметов:", max_points)
    print("Итоговые очки выживания:", final_score)

    # Проверяем существование положительного решения
    if final_score > 0:
        print("Решение существует")
    else:
        print("Положительного решения нет")


# Допзадание 2 - Все допустимые комбинации

def find_all_combinations():

    item_codes = list(items.keys())
    valid_combinations = []

    # Перебираем комбинации с разным количеством предметов
    for item_count in range(len(item_codes) + 1):

        #Генерируем комбинации предметов
        for selected_items in combinations(item_codes, item_count):

            #Считаем количество занятых ячеек
            used_cells = sum(items[code]['cells'] for code in selected_items)

            #Пропускаем комбинации, которые не помещаются
            if used_cells > MAX_CELLS:
                continue

            #Вычисляем итоговые очки выживания
            final_score = calculate_score(selected_items)

            #Сохраняем комбинации с положительным счётом
            if final_score > 0:
                valid_combinations.append((selected_items, used_cells, final_score))

    print("\nДопзадание 2 - Все допустимые комбинации")

    #Выводим все найденные комбинации
    for number, (selected_items, used_cells, final_score) in enumerate(valid_combinations, 1):
        print(
            f"{number}. {selected_items} | "
            f"Ячейки: {used_cells} | "
            f"Очки: {final_score}"
        )

    print("Всего комбинаций:", len(valid_combinations))


if __name__ == '__main__':
    check_7_cells()
    find_all_combinations()
