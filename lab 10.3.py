def read_queues_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            queues = [line.strip().split(', ') for line in file if line.strip()]
        if not queues:
            print("Файл пуст или содержит только пустые строки.")
            exit()
        return queues
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        exit()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        exit()


def print_queues(queues):
    print("Содержимое очередей:")
    for i, queue in enumerate(queues):
        print(f"Очередь {i + 1}: {', '.join(queue)}")

def interleave_queues(queues):
    result = []
    while any(queues):
        for queue in queues:
            if queue:
                result.append(queue.pop(0))
    return result


filename = input("Введите имя файла с очередями: ").strip()
try:
    queues = read_queues_from_file(filename)
    print_queues(queues)
    interleaved_result = interleave_queues(queues)
    print("Результат чередования:")
    print(', '.join(interleaved_result))
except Exception as e:
    print(f"Ошибка: {e}")