

def game():
    count = random.randint(4, 30)
    print(f"Начальное количество камней {count}")

    while count > 1:
        while 1:
            try:
                user_move = int(
                    input(f"У вас {count} камней. Введите количество камней (1, 2 или 3), которое вы хотите забрать: "))
            except ValueError:
                print("Введено неверное значение")
                continue
            else:
                break

        count -= user_move
        print(f"Осталось {count} камней")
        if count == 1:
            print("Вы выиграли!")
            break

        computer_move = random.randint(1, 3)
        count -= computer_move
        print(f"Компьютер взял {computer_move} камней. Осталось {count} камней.")

        if count == 1:
            print("Компьютер выиграл!")


game()