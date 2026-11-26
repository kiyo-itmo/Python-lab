# LAB 4 - Variant 4

MAX_CELLS = 9
START_POINTS = 15

items = {
    'r': {'points': 25, 'cells': 3},  # Винтовка - Súng trường
    'p': {'points': 15, 'cells': 2},  # Пистолет - Súng lục
    'a': {'points': 15, 'cells': 2},  # Боекомплект - Đạn dược
    'm': {'points': 20, 'cells': 2},  # Аптечка - Bộ cứu thương
    'i': {'points': 5, 'cells': 1},   # Ингалятор - Ống hít
    'k': {'points': 15, 'cells': 1},  # Нож - Dao
    'x': {'points': 20, 'cells': 3},  # Топор - Rìu
    't': {'points': 25, 'cells': 1},  # Оберег - Bùa hộ mệnh
    'f': {'points': 15, 'cells': 1},  # Фляжка - Bình nước
    'd': {'points': 10, 'cells': 1},  # Антидот - Thuốc giải độc
    's': {'points': 20, 'cells': 2},  # Еда - Thực phẩm
    'c': {'points': 20, 'cells': 2}   # Арбалет - Nỏ
}


# Tao bang quy hoach dong
def gen_table_memo(items, max_cells=MAX_CELLS):
    dp_table = [[0 for _ in range(max_cells)] for _ in range(len(items))]

    #Перебираем все предметы
    for item_index, item in enumerate(items.values()):
        item_points = item['points']
        item_cells = item['cells']

        for cell_index, current_capacity in enumerate(range(1, max_cells + 1)):

            if item_index == 0:
                dp_table[item_index][cell_index] = (0 if item_cells > current_capacity else item_points)
                continue

            skip_points = dp_table[item_index - 1][cell_index]

            if item_cells > current_capacity:
                dp_table[item_index][cell_index] = skip_points

            elif item_cells == current_capacity:
                dp_table[item_index][cell_index] = max(skip_points, item_points)

            else:
                remaining_points = dp_table[item_index - 1][cell_index - item_cells]
                dp_table[item_index][cell_index] = max(skip_points, remaining_points + item_points)

    return dp_table


# Tim cac vat pham duoc chon (Восстанавливаем выбранные предметы из таблицы)
def find_selected(dp_table, items, max_cells):
    item_codes = list(items.keys())  
    selected_items = []             #Список выбранных предметов
    cell_index = max_cells - 1      # Начинаем с последнего столбца

    for item_index in range(len(item_codes) - 1, -1, -1):
        if cell_index < 0:
            break

        if item_index == 0:
            if dp_table[item_index][cell_index] > 0:
                selected_items.append(item_codes[item_index])

        elif dp_table[item_index][cell_index] != dp_table[item_index - 1][cell_index]:   #Если значение отличается от предыдущей строки, значит предмет был выбран
            item_code = item_codes[item_index]
            selected_items.append(item_code)
            cell_index -= items[item_code]['cells']

    selected_items.reverse()  #Восстанавливаем исходный порядок предметов
    return selected_items


# Tinh diem sinh ton (Вычисляем итоговые очки выживания)
def calculate_score(selected_items):
    selected_points = sum(items[code]['points'] for code in selected_items)
    total_points = sum(item['points'] for item in items.values())

    final_score = START_POINTS + selected_points - (total_points - selected_points)

    return final_score


# Hien thi ba lo 3x3 (Выводим инвентарь в виде таблицы 3x3)
def show_inventory(selected_items):
    inventory = []

    #Каждый предмет занимает определённое количество ячеек
    for item_code in selected_items:
        item_cells = items[item_code]['cells']
        inventory.extend([item_code] * item_cells)

    while len(inventory) < MAX_CELLS:  #Заполняем пустые ячейки символом '-'
        inventory.append('-')

    for i in range(0, MAX_CELLS, 3):    #Выводим три строки по три ячейки
        print(','.join(f'[{code}]' for code in inventory[i:i + 3]))


if __name__ == '__main__':
    dp_table = gen_table_memo(items)
    selected_items = find_selected(dp_table, items, MAX_CELLS)
    final_score = calculate_score(selected_items)

    print("Вариант 4")
    print("Инвентарь:")
    show_inventory(selected_items)

    print("Итоговые очки выживания:", final_score)

    if final_score > 0:
        print("Решение найдено")
    else:
        print("Положительного решения нет")
