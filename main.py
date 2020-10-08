# Design and Analysis of Data Structures and Algorithms

import random
from algorithms.sort import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

numbers = random.sample(range(100, 999), 25)

print("Unsorted List")
print(numbers)

print("Bubble Sort")
bs = bubble_sort(numbers)
print(bs)

print("Selection Sort")
ss = selection_sort(numbers)
print(ss)

print("Insertion Sort")
ins = insertion_sort(numbers)
print(ins)

print("Merge Sort")
ms = merge_sort(numbers)
print(ms)

print("Quick Sort")
qs = quick_sort(numbers)
print(qs)