def read_words_from_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            words = file.read().strip().split()
            return [word.strip().lower() for word in words]
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
        return None


def check_word_in_file(word, words, file_name):
    if word not in words:
        print(f"Слово '{word}' отсутствует в файле {file_name}.")
        return False
    return True


def is_palindrome_logic(word):
    char_array = list(word)
    stack = []
    n = len(char_array)
    mid = n // 2

    for i in range(mid):
        stack.append(char_array[i])

    start = mid if n % 2 == 0 else mid + 1
    for i in range(start, n):
        if stack.pop() != char_array[i]:
            return False
    return True


def is_palindrome(word):
    file_name = "txt.txt"
    words = read_words_from_file(file_name)

    if words is None:
        return

    word = word.strip().lower()
    if not check_word_in_file(word, words, file_name):
        return

    if len(word) < 3:
        print(f"Слово '{word}' слишком короткое, чтобы быть палиндромом.")
        return

    if is_palindrome_logic(word):
        print(f"Слово '{word}' является палиндромом.")
    else:
        print(f"Слово '{word}' не является палиндромом.")

user_word = input("Введите слово для проверки: ").strip()
is_palindrome(user_word)
