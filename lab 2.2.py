def chek(str):
    if str.lstrip("-").isdigit():
        print("Число введено")
    else:
        print("Нужно число.")
        exit()


print("Введите число N:")
N = input()
chek(N)
print("Введите число M:")
M = input()
chek(M)
N = int(N)
M = int(M)
if len(str(abs(N))) > len(str(abs(M))):
    print("В числе N больше цифр")
elif len(str(abs(N))) == len(str(abs(M))):
    print("Количество цифр в числах равно")
else:
    print("В числе M больше цифр")