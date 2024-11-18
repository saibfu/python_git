def chek(string):
    if string.isdigit():
        print("Введено число")
    else:
        print("Нужно неотрицательное число, попробуйте снова.")
        exit()


print("Введите длины трех сторон треугольника: ")
a = input()
chek(a)
b = input()
chek(b)
c = input()
chek(c)
a = int(a)
b = int(b)
c = int(c)
if (a + b > c) and (b + c > a) and (a + c > b):
    print("треугольник существует")
else:
    print("треугольника не существует")
    exit()
if a ** 2 + b ** 2 < c ** 2:
    print("Треугольник тупоугольный")
if a ** 2 + b ** 2 > c ** 2:
    print("Треугольник остроугольный")
if a ** 2 + b ** 2 == c ** 2:
    print('st')

