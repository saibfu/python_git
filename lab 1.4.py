import math


def get_coordinate(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("введите корректное число.")


x = get_coordinate("Введите координату x: ")
y = get_coordinate("Введите координату y: ")
z = get_coordinate("Введите координату z: ")
length = math.sqrt(x ** 2 + y ** 2 + z ** 2)
print("Длина вектора с координатами ({}, {}, {}) равна {:.2f}".format(x, y, z, length))
