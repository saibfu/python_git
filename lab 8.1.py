def input_text(prompt):
    while True:
        text = input(prompt).strip()
        if not text:
            print("Ошибка: строка не должна быть пустой. Попробуйте снова.")
        else:
            return text

text = input_text("Введите строку текста: ")
unique_count = len(set(text))
print(f"Количество уникальных символов в строке: {unique_count}")