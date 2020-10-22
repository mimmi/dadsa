# Design and Analysis of Data Structures and Algorithms
# Push Test

import random
from algorithms.sort import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from algorithms.search import linear_search, binary_search, jump_search

#numbers = random.sample(range(100, 999), 899)
numbers = [10, 20, 30, 40, 50]

x = 10

#result = linear_search(numbers, x)
result = binary_search(numbers, x)
#result = jump_search(numbers, x, len(numbers)) 
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

'''
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
'''