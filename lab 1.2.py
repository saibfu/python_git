#третья переменная
while True:
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        break
    except ValueError:
        print("введите корректные числа.")

temp = a
a = b
b = temp

print("После обмена:")
print("a=", a)
print("b=", b)

#прямое уравнивание
while True:
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Пожалуйста, введите корректные числа.")

a, b = b, a

print("После обмена:")
print("Первое число:", a)
print("Второе число:", b)


#арифметическая операция
while True:
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Пожалуйста, введите корректные числа.")

a = a + b
b = a - b
a = a - b

print("После обмена:")
print("Первое число:", a)
print("Второе число:", b)