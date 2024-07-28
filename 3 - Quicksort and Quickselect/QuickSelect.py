"""
    Quick Select

    Function: Finds kth smallest element in list of integers
    Time Complexity (Worst): O(n)
    Space Complexity (Auxiliary): O(n)

"""

from Partition import partition
import MedianOfMedians as mom

def quick_select(array: list[int], k: int, start: int = None, end: int = None, isPreliminary: bool = True) -> int:

    # makes a copy of array and changes value of k to start at 1
    if isPreliminary:
        temp_array = array.copy()
        k -= 1
    else:
        temp_array = array

    # checks if start and end index have been inputted
    if start == None or end == None:
        start = 0
        end = len(temp_array) - 1

    # checks if end is after start
    if end > start:

        # partition array
        pivot_value = mom.median_of_medians(temp_array, start, end)
        pivot = partition(temp_array, start, end, pivot_value)

        # k is before pivot index
        if k < pivot:

            # quick selects on left side of pivot
            return quick_select(temp_array, k, start, pivot - 1, False)
        
        # k is after pivot index
        elif k > pivot:

            # quick selects on right side of pivot
            return quick_select(temp_array, k, pivot + 1, end, False)
        
        # k is on pivot index
        else:

            # returns element in index k
            return temp_array[k]
    else:

        # returns element in index k
        return temp_array[k]

if __name__ == '__main__':
    array = [3, 4, 1, 5, 2, 6, 10, 9, 7, 8]
    print(f"Array: {array}")
    k = 4
    print(f"{k}th smallest element: {quick_select(array, k)}")
    