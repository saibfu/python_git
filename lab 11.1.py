import os


def read_vector_from_file(filename):
    if not os.path.exists(filename):
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None

    with open(filename, 'r', encoding='utf-8') as file:
        try:
            return [float(num) for num in file.read().split()]
        except ValueError:
            print("Ошибка: Файл содержит некорректные данные. Ожидались только числа.")
            return None


def write_vector_to_file(filename, vector):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, vector)))


def truncate_vector(vector, num_to_remove):
    if not isinstance(vector, list):
        print("Ошибка: Вектор должен быть списком чисел.")
        return None
    if not all(isinstance(x, (int, float)) for x in vector):
        print("Ошибка: Все элементы вектора должны быть числами.")
        return None
    if not isinstance(num_to_remove, int) or num_to_remove < 0:
        print("Ошибка: Количество удаляемых элементов должно быть неотрицательным целым числом.")
        return None
    return vector[:-num_to_remove] if num_to_remove <= len(vector) else []


input_file = '../input.txt'
output_file = '../output.txt'
num_to_remove = 3

vector = read_vector_from_file(input_file)
if vector is not None:
    print(f"Исходный вектор: {vector}")
    truncated_vector = truncate_vector(vector, num_to_remove)
    if truncated_vector is not None:
        print(f"Обработанный вектор: {truncated_vector}")
        write_vector_to_file(output_file, truncated_vector)
        print(f"Результат записан в файл '{output_file}'.")
