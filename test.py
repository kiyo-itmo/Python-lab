import os
import math

CSI = "\x1b["
HEIGHT = 10          # số hàng của đồ thị (>= 9)
WIDTH = 40           # số cột
X_MAX = 16           # x chạy từ 0 đến 16 -> sqrt(16) = 4
Y_MAX = math.sqrt(X_MAX)

os.system("")                       # bật ANSI trên Windows
os.system("cls" if os.name == "nt" else "clear")

# Vẽ hai trục
for r in range(1, HEIGHT + 1):      # trục y (dọc)
    print(f"{CSI}{r};1H|")
print(f"{CSI}{HEIGHT + 1};1H" + "-" * WIDTH)   # trục x (ngang)

# Vẽ đồ thị
for col in range(2, WIDTH + 1):
    x = (col - 1) / (WIDTH - 1) * X_MAX
    y = math.sqrt(x)
    row = HEIGHT - round(y / Y_MAX * (HEIGHT - 1))
    print(f"{CSI}{row};{col}H{CSI}41m {CSI}0m", end="")

print(f"{CSI}{HEIGHT + 3};1H")        # đưa con trỏ xuống dưới