import os
import random


def read_phrases_from_file(filename):
    if not os.path.exists(filename):
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None

    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip().split('; ') for line in file]
    return lines


def generate_sentences(phrases, num_sentences):
    if not phrases or len(phrases) != 4:
        print("Ошибка: В файле должны быть 4 строки с фразами.")
        return None

    sentences = []
    for _ in range(num_sentences):
        sentence = f"{random.choice(phrases[0])} {random.choice(phrases[1])} {random.choice(phrases[2])} {random.choice(phrases[3])}"
        sentences.append(sentence)
    return sentences


def write_sentences_to_file(filename, sentences, append=False):
    mode = 'a' if append else 'w'
    with open(filename, mode, encoding='utf-8') as file:
        if append:
            file.write('\n\n')
        file.write('\n'.join(sentences))


input_file = '../Phrases.txt'
output_file = '../Result.txt'

phrases = read_phrases_from_file(input_file)
if not phrases:
    exit()

while True:
    try:
        num_sentences = int(input("Сколько предложений вы хотите сгенерировать? "))
        if num_sentences <= 0:
            print("Введите положительное число.")
            continue
    except ValueError:
        print("Ошибка: Введите целое число.")
        continue
    sentences = generate_sentences(phrases, num_sentences)
    if sentences:
        write_sentences_to_file(output_file, sentences, append=True)
        print(f"{num_sentences} предложений записано в файл '{output_file}'.")
    user_choice = input("Хотите продолжить генерацию? (Да/Нет): ").strip().lower()
    if user_choice == 'нет':
        print("Программа завершена.")
        break
