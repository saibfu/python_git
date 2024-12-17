import os

# Проверяем, существует ли файл
if not os.path.exists("../lab 12/task3.txt"):
    print("Ошибка: файл 'task3.txt' не найден.")
else:
    # Открываем файл и обрабатываем строки
    with open("../lab 12/task3.txt", encoding='utf-8') as f:
        raw_data = f.readlines()


    if not raw_data:
        print("Ошибка: файл 'task3.txt' пуст.")
    else:
        # Преобразуем строки в список кортежей
        people = []
        for line in raw_data:
            parts = line.split()
            if len(parts) != 2:  # Проверка, чтобы в строке было ровно два элемента
                print(f"Ошибка: некорректный формат строки: '{line.strip()}'. Ожидались фамилия и год.")
                continue
            surname, year = parts
            if not year.isdigit():  # Проверка, что год является числом
                print(f"Ошибка: некорректный год: '{year}' в строке '{line.strip()}'.")
                continue
            people.append((surname, int(year)))

        # Сортировка списка
        sorted_people = sorted(people, key=lambda x: (x[0], x[1]))

        # Вывод результата
        for surname, year in sorted_people:
            print(surname, year)