import re

number = input("Введите номер автомобиля: ")

if re.fullmatch(r"[A-Za-z]{2}\d{3}[A-Za-z]", number):
    print(f"{number} может принадлежать автомобилю")
else:
    print(f"{number} не может принадлежать автомобилю")