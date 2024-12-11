def scalar_product(vector1, vector2):
    product = 0
    for i in range(len(vector1)):
        product += vector1[i] * vector2[i]
    return product

def get_vector_input(prompt):
    while True:
        vector_str = input(prompt)
        try:
            vector = list(map(int, vector_str.split()))
            return vector
        except ValueError:
            print("Некорректный ввод. Введите только числа.")


vector1 = get_vector_input("Введите элементы первого вектора, разделённые пробелом: ")
vector2 = get_vector_input("Введите элементы второго вектора, разделённые пробелом: ")

if not (len(vector1) != len(vector2)):
    print("Скалярное произведение векторов: не определено")
else:
    result = scalar_product(vector1, vector2)
    print(f"Скалярное произведение векторов: {result}")