
import os
import time

CSI = "\x1b["
ZERO = CSI + "0G"
ERASE = CSI + "2K"
RESET = CSI + "0m"

# Цвета (256-color mode)

BROWN = 130           # коричневый (ствол)


SIZE = 9              # высота ёлки

frames_colors = []
def draw_line(offset, filled, color):
    """Рисует одну строку: отступ + цветной блок."""
    offset_part = " " * offset
    filled_part = f"{CSI}48;5;{color}m" + " " * filled
    line = f"{ERASE}{offset_part}{filled_part}{RESET}"
    print(line)


def draw_tree(n, colors):
    """
    Рисует ёлку высотой n.

    Параметры:
        n+2      — высота ёлки
        colors — список цветов для каждого уровня
    """
    # === Крона ===
    for i in range(1, n + 1):
        offset = n - i
        filled = 2 * i - 1
        #color = colors[(i - 1) % len(colors)]
        draw_line(offset, filled, colors)

    # === Ствол ===
    for _ in range(2):
        offset = n - 2
        filled = 3
        draw_line(offset, filled, BROWN)


def animate():
   colors = range(46,49)
   t=10
   while t>0:
        for color in colors:
            os.system("cls" if os.name == "nt" else "clear")
            draw_tree(SIZE, color)
            #print(f"{CSI}{SIZE+2}A{ZERO}", end="", flush=True)
            time.sleep(0.5)
        t-=1
    

   

if __name__ == "__main__":
    animate()