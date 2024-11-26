line_1 = input("Введите первую строку: ")
line_2 = input("Введите вторую строку: ")

line_1 = line_1.replace(line_2, "", line_1.count(line_2) - 1)

print(f"Строка после исключений: {line_1}")