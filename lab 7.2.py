def input_matrix(rows, cols, matrix_num):
    matrix = []
    print(f"Введите элементы матрицы {matrix_num} размером {rows}×{cols} (вводите элементы через пробел):")
    for _ in range(rows):
        while True:
            row = input().strip().split()
            if len(row) != cols:
                print(f"Ошибка ввода. Должно быть {cols} элементов.")
                continue
            try:
                row = [float(num) for num in row]
                matrix.append(row)
                break
            except ValueError:
                print("Ошибка ввода. Убедитесь, что все элементы — числа.")
    return matrix


def get_positive_int(prompt):
    while True:
        value = input(prompt)
        if not value.isdigit() or int(value) <= 0:
            print("Ошибка ввода. Введите положительное целое число.")
        else:
            return int(value)


def multiply_matrices(matrix1, matrix2):
    M, K = len(matrix1), len(matrix1[0])
    K2, N = len(matrix2), len(matrix2[0])
    result = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            for k in range(K):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


M = get_positive_int("Введите число строк первой матрицы (M): ")
K1 = get_positive_int("Введите число столбцов первой матрицы (K): ")
K2 = get_positive_int("Введите число строк второй матрицы (K): ")
N = get_positive_int("Введите число столбцов второй матрицы (N): ")
if K1 != K2:
    print("Ошибка: Число столбцов первой матрицы должно быть равно числу строк второй матрицы для умножения.")
else:
    matrix1 = input_matrix(M, K1, "1")
    matrix2 = input_matrix(K2, N, "2")
    result = multiply_matrices(matrix1, matrix2)
    print("\nРезультат умножения матриц:")
    for row in result:
        print(f"[{', '.join(map(str, row))}]")