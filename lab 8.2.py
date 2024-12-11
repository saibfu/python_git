def input_text(prompt):
    while True:
        text = input(prompt).strip()
        if not text:
            print("Ошибка: строка не должна быть пустой. Попробуйте снова.")
        else:
            return text


def find_unique_characters_in_order(str1, str2):
    unique_chars = []  # Список для хранения уникальных символов
    for char in str1:
        if char not in str2:  # Проверяем, есть ли символ из первой строки во второй
            unique_chars.append(char)
    return unique_chars

str1 = input_text("Введите первую строку текста: ")
str2 = input_text("Введите вторую строку текста: ")

unique_chars = find_unique_characters_in_order(str1, str2)

if unique_chars:
    quoted_chars = [f"'{char}'" for char in unique_chars]
    print(f"Символы, которые встречаются в первой строке, но не встречаются во второй: {', '.join(quoted_chars)}")
else:
    print("В первой строке нет символов, которые не встречаются во второй.")