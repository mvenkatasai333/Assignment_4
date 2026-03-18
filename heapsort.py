import random
import time
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Better pivot choice: middle element
    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result
def measure_time(sort_function, data):
    start = time.perf_counter()
    result = sort_function(data)
    end = time.perf_counter()
    return end - start, result
def test_sorting():
    sizes = [100, 500, 1000]

    for size in sizes:
        print("\nTesting size:", size)
        random_data = [random.randint(1, 1000) for _ in range(size)]
        sorted_data = list(range(size))
        reverse_data = list(range(size, 0, -1))

        test_cases = [
            ("Random", random_data),
            ("Sorted", sorted_data),
            ("Reverse", reverse_data)
        ]

        for name, data in test_cases:
            print("\nData type:", name)

            heap_time, heap_result = measure_time(heap_sort, data)
            print("Heapsort time:", round(heap_time, 6), "seconds")

            quick_time, quick_result = measure_time(quick_sort, data)
            print("Quicksort time:", round(quick_time, 6), "seconds")

            merge_time, merge_result = measure_time(merge_sort, data)
            print("Merge Sort time:", round(merge_time, 6), "seconds")

            correct = sorted(data)
            if heap_result != correct:
                print("Heapsort result is incorrect")
            if quick_result != correct:
                print("Quicksort result is incorrect")
            if merge_result != correct:
                print("Merge Sort result is incorrect")
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    sorted_arr = heap_sort(arr)
    print("Sorted array:", sorted_arr)

    test_sorting()