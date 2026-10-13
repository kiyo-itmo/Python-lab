BLOCK = "#"


def make_row(width, positions):
    """Строка из пробелов с блоками в заданных позициях."""
    row = [" "] * width
    for p in positions:
        row[p] = BLOCK
    return "".join(row)


def make_pattern(width):
    """Один узор "d" (7 строк) для заданной ширины."""
    if width % 2 == 0:      # ширина должна быть нечётной,
        width += 1          # чтобы блок был ровно по центру

    full = BLOCK * width
    center = make_row(width, [width // 2])
    two = make_row(width, [width // 4, width - 1 - width // 4])

    return [full, center, center, full, two, two, full]


def draw_pattern(width=17, count_x=4, count_y=3):
    """Рисует узор: count_x раз вбок, count_y раз вниз."""
    pattern = make_pattern(width)
    
    for _ in range(count_y):
        for line in pattern:
            print(line * count_x)


if __name__ == "__main__":
    draw_pattern(width=25, count_x=1, count_y =0)


