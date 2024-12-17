import os

def read_file(filename):
    if not os.path.exists(filename):
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def extract_table_of_contents(lines):
    chapters = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "":
            i += 1
            continue

        if lines[i].startswith("Глава") or lines[i].startswith("Chapter"):
            chapter_info = lines[i].strip()
            i += 1
            if i < len(lines):
                title = lines[i].strip()
                chapters.append(f"{chapter_info}. {title}")
        i += 1

    return chapters

def write_table_of_contents(filename, contents):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Оглавление\n")
        file.write("\n".join(contents))

input_file = '../book.txt'
output_file = '../table_of_contents.txt'

lines = read_file(input_file)
if lines:
    contents = extract_table_of_contents(lines)
    write_table_of_contents(output_file, contents)
    print(f"Оглавление записано в файл '{output_file}'.")