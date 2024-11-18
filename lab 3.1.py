import math

try:
    print("Введите целое число градусов для переменной n: ")
    n = float(input())
except ValueError:
    print("Вы ввели не число")
    exit()
# пребразование в радианы
n_rad = n * math.pi / 180
print("cos = ", math.cos(n_rad))
print("sin = ", math.sin(n_rad))
print("tan = ", math.tan(n_rad))