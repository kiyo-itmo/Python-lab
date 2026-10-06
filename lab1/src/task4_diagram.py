"""
Задание 4 (Вариант 4): Диаграмма процентного соотношения.

Условие: среднее по модулю первых 125 и вторых 125 чисел.
"""

from pathlib import Path

# Цвета
BLUE = '\033[44m'    # синий фон
RED = '\033[41m'     # красный фон
END = '\033[0m'      # сброс цвета


# Путь к файлу: từ src/ lùi lên 1 cấp, vào data/sequence.txt
DATA_FILE = Path(__file__).parent.parent / "data" / "sequence.txt"


def read_file():
    """Читает файл sequence.txt → список чисел."""
    with open(DATA_FILE, "r") as f:
        return [float(line) for line in f if line.strip()]


def draw_bar(value, total, color):
    """Рисует одну полоску. Длина = 50 ký tự."""
    percent = value / total * 100
    cells = int(percent / 2)   # 100% = 50 ký tự → 1% = 0.5 ký tự
    print(f"{color}{' ' * cells}{END} {percent:.2f}%")


def main():
    # 1. Đọc file
    data = read_file()
    print(f"Всего чисел: {len(data)}")

    # 2. Tách 2 nhóm: 125 đầu và 125 sau
    group_1 = data[:125]
    group_2 = data[125:250]

    # 3. Tính trung bình giá trị tuyệt đối
    avg_1 = sum(abs(x) for x in group_1) / len(group_1)
    avg_2 = sum(abs(x) for x in group_2) / len(group_2)

    print(f"Группа 1: среднее = {avg_1:.4f}")
    print(f"Группа 2: среднее = {avg_2:.4f}")

    # 4. Tính tổng để chia phần trăm
    total = avg_1 + avg_2

    # 5. Vẽ biểu đồ
    print("\nДиаграмма:")
    draw_bar(avg_1, total, BLUE)
    draw_bar(avg_2, total, RED)


if __name__ == "__main__":
    main()