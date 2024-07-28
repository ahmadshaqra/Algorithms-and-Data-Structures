"""
    Median of Medians

    Function: Finds the median of medians in a list of integers
    Time Complexity (Worst): O(n)
    Space Complexity (Auxiliary): O(log(n))

"""

import QuickSelect as qs
from _.InsertionSort import insertion_sort

def median_of_medians(array: list[int], start: int = None, end: int = None) -> int:

    # checks if start and end index have been inputted
    if start == None or end == None:
        start = 0
        end = len(array) - 1

    # checks if array size is already less than or equal to 5
    if (end - start + 1) <= 5:

        # makes a copy of the array
        temp_array = array[start : end + 1]

        # finds the median
        insertion_sort(temp_array)
        return temp_array[(len(temp_array) - 1) // 2]
    
    # creates empty array of medians
    medians = []

    # traverses subgroups of array
    for i in range((end - start + 1) // 5):
        sub_array = array[5 * i + start : 5 * i + 5 + start]

        # finds the median and appends it to medians array
        insertion_sort(sub_array)
        medians.append(sub_array[2])
    
    # returns median of medians
    return qs.quick_select(medians, (len(medians) + 1) // 2)

if __name__ == '__main__':
    array = [3, 4, 1, 5, 2, 6, 10, 9, 7, 8, 12, 11, 13, 10, 14, 18, 19, 16, 17, 20]
    print(f"Array: {array}")
    print(f"Median of Medians: {median_of_medians(array)}")
