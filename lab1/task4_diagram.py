CSI = '\x1b['
RED= CSI +"41m"  # красный фон
BLUE= CSI +"44m" # синий фон
RESET= CSI +"0m"   # сброс цвета

    
with open("sequence.txt") as f:
    data = [float(line) for line in f if line.strip()]

group_1 = data[:125]
group_2 = data[125:250]

avg_1 = sum(abs(x) for x in group_1) / 125
avg_2 = sum(abs(x) for x in group_2) / 125

p1 = avg_1 / (avg_1 + avg_2) * 100
p2 = 100 - p1

print('первые 125:',BLUE + ' '*round(p1) + RESET + '%.2f%%' % p1)
print('вторые 125:',RED + ' '*round(p2) + RESET + '%.2f%%' % p2)