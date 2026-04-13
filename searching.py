import json

from generators import unordered_sequence
from generators import unordered_sequence, dna_sequence, ordered_sequence

# def read_data(file_name, field):
#     try:
#         with open(file_name, "r", encoding="utf-8") as f:
#             data = json.load(f)
#     except:
#         return None
#     return data.get(field, None)
# def linear_search(seq, num) -> dict:
#     bambus = []
#     for index, wanted in enumerate(seq):
#         if wanted == num:
#             bambus.append(index)
#     return  {
#         "position": bambus,
#         "count": len(bambus)
#     }
# def binary_search(seq, target):
#     seq.sort()
#     left = 0
#     right = len(seq) - 1
#     if target not in seq:
#         return None
#     else:
#         while left <= right:
#             mid = (left + right) // 2
#             mid_value = seq[mid]
#
#             if mid_value == target:
#                 return mid
#             elif mid_value < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#         return None

import time
import matplotlib.pyplot as plt

def read_data(file_name, field):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return None
    return data.get(field, None)
def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return None

def pattern_search(sequence, pattern):
    positions = set()
    n = len(sequence)
    m = len(pattern)

    if m == 0 or m > n:
        return positions

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if sequence[i + j] != pattern[j]:
                match = False
                break

        if match:
            positions.add(i)

    return positions

def main():

    unordered_data = read_data("sequential.json","unordered_numbers")
    ordered_data = read_data("sequential.json","ordered_numbers")
    dna_data = read_data("sequential.json", "dna_sequence")
    print("========Linear=======")
    print(linear_search(unordered_data, 9))
    print("========Binar=========")
    print(binary_search(ordered_data, 5))
    print("========Pattern==========")
    print(pattern_search(dna_data, "ATA"))
    print("========Grafs===========")
    sizes = [100, 500, 1000, 5000, 10000, 20000, 50000]
    linear_times = []
    binary_times = []
    set_times = []
    REPEATS = 500
    print("Bambus. . .")

    for size in sizes:
        data_list = list(range(size))

        data_set = set(data_list)

        target = -1

        start = time.perf_counter()
        for _ in range(REPEATS):
            linear_search(data_list, target)
        end = time.perf_counter()
        linear_times.append((end - start) / REPEATS)

        start = time.perf_counter()
        for _ in range(REPEATS):
            binary_search(data_list, target)
        end = time.perf_counter()
        binary_times.append((end - start) / REPEATS)

        start = time.perf_counter()
        for _ in range(REPEATS):
            _ = target in data_set
        end = time.perf_counter()
        set_times.append((end - start) / REPEATS)

    print("Bambus done@#$%@#^@#&$%^@$")
    print("=========End===========")
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, label='Sekvenční (list)', marker='o', color='red')
    plt.plot(sizes, binary_times, label='Binární (list)', marker='s', color='blue')
    plt.plot(sizes, set_times, label='Hashovací (set)', marker='^', color='green')

    plt.xlabel("Velikost vstupu (počet prvků) - N")
    plt.ylabel("Průměrný čas běhu [s]")
    plt.title("Porovnání časové složitosti vyhledávacích algoritmů")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.show()

if __name__ == "__main__":
    main()

