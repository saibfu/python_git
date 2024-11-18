def chek(string):
    if string.isdigit():
        print("Спасибо что ввели число!")
    else:
        print("Нужно число.")
        exit()
    if int(string) < 100000 or int(string) > 999999:
        print("Введен не шестизначный номер")
        exit()


print("Введите M - больший шестизначный номер билета: ")
M = input()
chek(M)
print("Введите N - наименьший шестизначный номер билета: ")
N = input()
chek(N)
M = int(M)
N = int(N)
if N > M:
    print("N должно быть меньше, чем M")
    exit()
count = 0
for numbers in range(N, M + 1):
    n1 = numbers % 10
    numbers = numbers // 10
    n2 = numbers % 10
    numbers = numbers // 10
    n3 = numbers % 10
    numbers = numbers // 10
    n4 = numbers % 10
    numbers = numbers // 10
    n5 = numbers % 10
    numbers = numbers // 10
    n6 = numbers % 10
    if (n6 + n5 + n4) == (n3 + n2 + n1):
        count += 1
print(count)
