"""
    Quick Sort

    Function: Sorts list of integers (unstable)
    Time Complexity (Average): O(n*log(n))
    Space Complexity (Auxiliary): O(log(n))

"""

from .Partition import partition

def quick_sort(array: list[int], start: int = None, end: int = None) -> None:
    
    # checks if start and end index have been inputted
    if start == None or end == None:
        start = 0
        end = len(array) - 1

    # checks if array contains at least two elements to be sorted
    if (end - start) > 1:

        # partitions array section and gets pivot index
        pivot = partition(array, start, end)

        # recursively sorts left and right side of array
        quick_sort(array, start, pivot)
        quick_sort(array, pivot + 1, end)

if __name__ == '__main__':
    array = [3, 4, 1, 5, 2, 6, 10, 9, 7, 8]
    print(f"Before Sort: {array}")
    quick_sort(array)
    print(f"After Sort: {array}")
    