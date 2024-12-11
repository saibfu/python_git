# Функция для разложения цикла в транспозиции
def cycle_to_transpositions(cycle):
    transpositions = []
    # Разбиваем цикл на транспозиции
    while len(cycle) > 1:
        transpositions.append((cycle[0], cycle[1]))
        cycle = [cycle[0]] + cycle[2:]
    return transpositions


# Функция для разложения подстановки в произведение транспозиций
def permutation_to_transpositions(perm):
    # Преобразуем подстановку в циклическую форму
    visited = [False] * len(perm)
    transpositions = []

    # Проходим по каждому элементу подстановки
    for i in range(len(perm)):
        if not visited[i]:
            cycle = []
            j = i
            # Формируем цикл, начиная с элемента i
            while not visited[j]:
                cycle.append(j + 1)  # Добавляем к циклу (нумерация с 1)
                visited[j] = True
                j = perm[j] - 1  # Переходим к следующему элементу цикла
            # Разлагаем цикл на транспозиции
            transpositions.extend(cycle_to_transpositions(cycle))

    return transpositions


# Функция для вывода транспозиций
def print_transpositions(transpositions):
    print("Произведение транспозиций:")
    for trans in transpositions:
        print(f"({trans[0]} {trans[1]})", end=" ")
    print()


# Ввод подстановки
def input_permutation():
    n = int(input("Введите количество элементов в подстановке: "))
    perm = list(map(int, input(f"Введите подстановку (например, 3 1 2 4 для 4 элементов): ").split()))
    return perm


# Основная часть программы
if __name__ == "__main__":
    # Ввод подстановки
    perm = input_permutation()

    # Разложение подстановки в транспозиции
    transpositions = permutation_to_transpositions(perm)

    # Вывод транспозиций
    print_transpositions(transpositions)