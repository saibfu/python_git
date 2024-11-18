def chek(string):
    if string.isdigit():
        print("Число введено")
    else:
        print("Нужно неотрицательное число.")
        exit()


print("Введите число, факториал которого нужно найти:")
N = input()
chek(N)
N = int(N)
a = 1
for i in range(1, N + 1):
    a *= i
print(a)
