import os


def sort_strings_by_a(file_path):
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл '{file_path}' не существует.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]
        sorted_lines = sorted(lines, key=lambda line: line.lower().count('а'), reverse=True)
        for line in sorted_lines:
            print(line)
    except UnicodeDecodeError:
        print(f"Ошибка: Невозможно прочитать файл '{file_path}', неверная кодировка.")


file_path = '../lab 12/file_path.txt'
sort_strings_by_a(file_path)