def input_array():
    while True:
        try:
            user_input = input("Введите элементы массива, разделённые пробелом: ")
            array = list(map(int, user_input.split()))
            if array:
                return array
            else:
                print("Ошибка ввода. Массив не может быть пустым.")
        except ValueError:
            print("Ошибка ввода. Убедитесь, что вы вводите только целые числа.")



def find_mode(array):
    frequency = {}
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]
    if len(modes) == 1:
        return modes[0]
    else:
        return None


array = input_array()
mode = find_mode(array)

if mode:
    print(f"Мода массива: {mode}")
else:
    print("Массив не имеет моды.")
