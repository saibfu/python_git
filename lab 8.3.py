def input_numbers(prompt):
    while True:
        try:
            numbers = input(prompt).strip().split()
            numbers = set(int(num) for num in numbers)
            return numbers
        except ValueError:
            print("Ошибка ввода. Введите только числа, разделенные пробелами.")


set1 = input_numbers("Введите первый набор чисел, разделенных пробелами: ")
set2 = input_numbers("Введите второй набор чисел, разделенных пробелами: ")
common_elements = set1 & set2
if common_elements:
    print(f"Числа, которые встречаются в обоих наборах: {', '.join(map(str, sorted(common_elements)))}")
else:
    print("Нет чисел, которые встречаются в обоих наборах.")
    1234
    2345

    |
    & 23 4
    - 1
    ^ 1 5