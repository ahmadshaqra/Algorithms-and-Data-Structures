"""
    Extras - Test Sorts

    Function: Tests speed of sorting algorithms

"""

from random import shuffle
from time import time
from _.CountingSort import counting_sort
from _.RadixSort import radix_sort
from _.QuickSort import quick_sort
from _.MergeSort import merge_sort
from _.SelectionSort import selection_sort
from _.InsertionSort import insertion_sort
from _.BubbleSort import bubble_sort
from typing import Callable

def test_sorts(sorting_algorithms: list[Callable], size: int) -> None:

    # creates array of inputted size
    print("\n... Creating Array ...")
    array = [i for i in range(size)]

    # tests each sorting algorithm individually
    for sorting_algorithm in sorting_algorithms:
        
        # shuffles array
        print("... Shuffling Array ...")
        shuffle(array)

        # displays sorting algorithm name
        name = sorting_algorithm.__name__
        name = name.upper()
        name = name.replace('_', ' ')
        print(f"\n[[ {name} ]]")
        
        # sorts array
        print("... Sorting Array ...")
        start_time = time()
        sorting_algorithm(array)
        end_time = time()

        # verifies array
        is_sorted = verify_sort(array)

        # displays result
        print(f"Sorted: {is_sorted}")
        print(f"Items Sorted: {len(array)}")
        print(f"Time Taken: {round(end_time - start_time, 3)}s\n")

def verify_sort(array: list[int]) -> bool:

    # verifies array is sorted
    print("... Verifying Sort ...")
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            return False
    return True

if __name__ == '__main__':
    sorting_algorithms = [sorted, counting_sort, radix_sort, quick_sort, merge_sort, selection_sort, insertion_sort, bubble_sort]
    size = 100000
    test_sorts(sorting_algorithms, size)
    