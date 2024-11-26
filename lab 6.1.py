import re
while True:
    line = input("Введите имя файла: ")
    if line == "":
        break
    if re.fullmatch(r"[^></|\\?*]*\.(txt|doc|docx|odt|rtf)", line):
        print(line, 'может быть именем файла')
    else:
        print(line, 'не может быть именем файла')