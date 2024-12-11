def add(dictionary, author, book):
    optional_author = dictionary.get(author, None)
    if optional_author == None:
        dictionary[author] = list()
    dictionary[author].append(book)

def print_author(dictionary, author):
    if dictionary.get(author, None) == None:
        print("Автор не найден")
    else:
        print(dictionary[author])

authors = {}
add(authors, "Test", "Book")
print_author(authors, "Test")

while True:
    message = input("print - вывод книг автора, add - добавить автора в словарь, exit - выйти из программы: ")
    if message == "add":
        author = input("Введите автора: ")
        book = input("Введите книгу автора: ")
        add(authors,author,book)
    elif message == "print":
        author = input("Введите автора: ")
        print_author(authors,author)
    elif message == "exit":
        break