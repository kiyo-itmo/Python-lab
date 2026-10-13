import os
import time

CSI = "\x1b["
ERASE = CSI + "2K"
RESET = CSI + "0m"

BROWN = 130   # коричневый (ствол)
SIZE = 9      # высота кроны


def draw_line(offset, filled, color):
    """Рисует одну строку: отступ + цветной блок."""
    print(f"{ERASE}{' ' * offset}{CSI}48;5;{color}m{' ' * filled}{RESET}")


def draw_tree(n, color):
    """Рисует ёлку: крона высотой n одного цвета + ствол."""
    # Крона
    for i in range(1, n + 1):
        draw_line(n - i, 2 * i - 1, color)

    # Ствол
    for _ in range(2):
        draw_line(n - 2, 3, BROWN)


def animate():
    colors = [34, 40, 46]            # 3 кадра: три оттенка зелёного
    for _ in range(5):              # 5 циклов
        for color in colors:
            os.system("cls" if os.name == "nt" else "clear")
            print(CSI + "H", end="")
            draw_tree(SIZE, color)
            time.sleep(0.5)


if __name__ == "__main__":
    os.system("")                    # включает ANSI в Windows
    animate()
