def chek(string):
    if string.isdigit():
        print("Число введено")
    else:
        print("Нужно неотрицательное число.")
        exit()
    if int(string) > 27 or int(string) == 0:
        print("Данной суммы цифр в трехзначном числе не существует")
        exit()


print("Введите сумму цифр в трёхзначном числе: ")
a = input()
chek(a)
a = int(a)
for i in range(100, 1001):
    i1 = i % 10
    i = i // 10
    i2 = i % 10
    i = i // 10
    i3 = i % 10
    if (i3 + i2 + i1) == a:
        print(i3, i2, i1)
