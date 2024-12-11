dictionary = dict()
dictionary["разделить"] = "split"
dictionary["вода"] = "water"
string = input("Введите строку: ")
array = string.split(" ")
for word in array:
    optional = dictionary.get(word, None)
    if optional == None:
        print(word, end=" ")
    else:
        print(dictionary[word], end=" ")