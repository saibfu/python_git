import math

try:
    print("Введите целое число a: ")
    a = int(input())
except ValueError:
    print("Вы ввели не целое число")
    exit()
try:
    print("Введите целое число b: ")
    b = int(input())
except ValueError:
    print("Вы ввели не целое число")
    exit()


# NOD - наибольший общий делитель
def nod():
    if a < b:
        ab = b
    else:
        ab = a
    for i in range(1, ab + 1):
        if a % i == 0 and b % i == 0:
            nod = i
    return nod


print("Наибольший общий делитель: ", nod())
print("Наибольший общий делитель из math: ", math.gcd(a, b))

if math.gcd(a, b) == nod():
    print("Всё верно")