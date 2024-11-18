import random

def print_welcome():
    print("Добро пожаловать в игру с камнями!")
    print("Правила: Каждый игрок по очереди забирает 1, 2 или 3 камня.")
    print("Выигрывает тот, кто оставит последнего камня своему сопернику.")

def print_stones(stones):
    print(f"Осталось {stones} камней.")

def user_turn(stones):
    while True:
        try:
            take = int(input("Сколько камней вы хотите взять? (1, 2 или 3): "))
            if take in [1, 2, 3] and take <= stones:
                stones -= take
                break
            else:
                print(f"Ошибка! Вы можете взять не более {stones} камней и только 1, 2 или 3 камня.")
        except ValueError:
            print("Пожалуйста, введите число.")
    return stones

def computer_turn(stones):
    take = random.randint(1, 3)
    if take > stones:
        take = stones
    print(f"Компьютер берёт {take} камней.")
    stones -= take
    return stones

def game():
    stones = random.randint(4, 30)  # Инициализация случайного количества камней от 4 до 30
    print_welcome()
    print_stones(stones)

    while stones > 0:
        # Ход пользователя
        stones = user_turn(stones)
        print_stones(stones)
        if stones == 0:
            print("Поздравляем, вы выиграли!")
            break

        # Ход компьютера
        stones = computer_turn(stones)
        print_stones(stones)
        if stones == 0:
            print("Компьютер выиграл! Повезёт в следующий раз.")
            break

if __name__ == "__main__":
    game()
