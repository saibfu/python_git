import os

def read_text_from_file(filename):
    if not os.path.exists(filename):
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None

    with open(filename, 'r', encoding='utf-8') as file:  # Указываем кодировку UTF-8
        return file.read().strip()


def write_sentences_to_file(filename, sentences):
    with open(filename, 'w', encoding='utf-8') as file:  # Указываем кодировку UTF-8
        file.write('\n'.join(sentences))

def filter_sentences_by_word_count(text, min_word_count):
    if not isinstance(min_word_count, int) or min_word_count <= 0:
        print("Ошибка: Минимальное количество слов должно быть положительным целым числом.")
        return None

    import re
    sentences = re.split(r'(?<=[.!?])\s+', text)
    filtered_sentences = [
        sentence for sentence in sentences
        if len(sentence.split()) > min_word_count
    ]
    return filtered_sentences

input_file = '../source_text.txt'
output_file = '../filtered_sentences.txt'

text = read_text_from_file(input_file)
if text:
    print(f"Исходный текст: {text}")
    try:
        min_word_count = int(input("Введите минимальное количество слов в предложении: "))
    except ValueError:
        print("Ошибка: Введите корректное целое число.")
    else:
        filtered_sentences = filter_sentences_by_word_count(text, min_word_count)
        if filtered_sentences:
            print(f"Отфильтрованные предложения:\n{filtered_sentences}")
            write_sentences_to_file(output_file, filtered_sentences)
            print(f"Результат записан в файл '{output_file}'.")
        else:
            print("Нет предложений, соответствующих заданному количеству слов.")