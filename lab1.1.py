def chek(string):
    if string.isdigit():
        print("Введено число")
    else:
        print("Нужно неотрицательное число. Попробуйте снова")
        exit()


print("Введите оклад первого сотрудника:")
salary = input()
chek(salary)
prize = float(salary) * 2 / 3
print(" Премия первого: ", prize)
