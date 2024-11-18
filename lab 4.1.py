def n_member_of_geometrical_progression(initial, diff, amount):
    if amount == 1:
        return initial
    else:
        return n_member_of_geometrical_progression(initial * diff, diff, amount - 1)

def sum_n_member_of_geometrical_progression(initial, diff, amount, sum):
    sum += initial
    initial *= diff
    if amount == 1:
        return sum
    else:
        return sum_n_member_of_geometrical_progression(initial, diff, amount - 1, sum)

def n_member_of_arifmethical_progression(initial, diff, amount):
    if amount == 1:
        return initial
    else:
        return n_member_of_arifmethical_progression(initial + diff, diff, amount - 1)

def dec_to_bin(n):
    if n == 0:
        return ''
    else:
        return dec_to_bin(n // 2) + str(n % 2)

def smallest_common_multiplier(a, b, c):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    gcd_value = gcd(a, b)
    return abs(a * b) // gcd_value

def get_option():
    print("1 - n элемент геометрической прогрессии")
    print("2 - сумма n элементов геометрической прогрессии")
    print("3 - n элемент алгебраической последовательности")
    print("4 - из десятичной СИ в двоичную")
    print("5 - наименьший общее кратное")
    print("0 - ВЫйТИ")
    return input("Выберите функцию: ")

def safe_int_input(message):
    number = 0
    try:
        number = int(input(message))
    except ValueError:
        print("Ошибка!")
    return number

option = "0"
while True:
    option = get_option()
    if option == "0":
        break
    elif option == "1" or option == "2" or option == "3":
        initial = safe_int_input("Введите начальное значение: ")
        diff = safe_int_input("Введите множитель прогрессии: ")
        amount = safe_int_input("Введите шаг: ")
        if option == "1":
            print("n элемент геометрической прогрессии:", n_member_of_geometrical_progression(initial, diff, amount))
        elif option == "2":
            print("сумма n элементов геометрической прогресии:", sum_n_member_of_geometrical_progression(initial, diff, amount, 0))
        else:
            print("n элемент алгебраической прогрессии:", n_member_of_arifmethical_progression(initial, diff, amount))
    elif option == "4":
        dec = safe_int_input("Десятичное число: ")
        print("Для числа", dec, "является двоичной записью число", dec_to_bin(dec))
    elif option == "5":
        a = safe_int_input("Введите первое число: ")
        b = safe_int_input("Введите второе число: ")
        print("наименьший общий делитель: ", smallest_common_multiplier(a, b, 1))
    else:
        print("Попытайся снова!")