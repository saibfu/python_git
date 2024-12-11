def invert_string():
    try:
        input_string = input("Введите строку для инверсии: ").strip()
        if not input_string:
            raise ValueError("Пустая строка недопустима.")

        stack = []
        for char in input_string:
            stack.append(char)

        inverted_string = ""
        while stack:
            inverted_string += stack.pop()

        print(f"Инвертированная строка: {inverted_string}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


invert_string()
