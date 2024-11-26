line = input("Введите строку: ")

line = line.strip().capitalize().strip(r"[!\.\?]{3}") + "."
print(line)