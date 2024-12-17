import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def compare_sorting_times():
    num_trials = 500
    array_size = 100

    bubble_sort_times = []
    standard_sort_times = []

    for _ in range(num_trials):
        arr = [random.randint(0, 10000) for _ in range(array_size)]
        start_time = time.time()
        bubble_sort(arr.copy())
        bubble_sort_times.append(time.time() - start_time)
        start_time = time.time()
        sorted(arr.copy())
        standard_sort_times.append(time.time() - start_time)

    avg_bubble_sort_time = sum(bubble_sort_times) / num_trials
    avg_standard_sort_time = sum(standard_sort_times) / num_trials

    print(f"Среднее время пузырьковой сортировки: {avg_bubble_sort_time:.6f} секунд")
    print(f"Среднее время стандартной сортировки: {avg_standard_sort_time:.6f} секунд")

compare_sorting_times()
