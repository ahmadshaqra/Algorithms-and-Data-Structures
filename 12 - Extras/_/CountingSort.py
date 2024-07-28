"""
    Counting Sort

    Function: Sorts list of integers
    Time Complexity (Worst): O(n+u)
    Space Complexity (Auxiliary): O(u)

"""

from typing import TypeVar
T = TypeVar('T')

def counting_sort(array: list[int]) -> None:

    # creates array of size max element
    max_element = max(array)
    count = [0] * (max_element + 1)

    # increment count for each element in array
    for element in array:
        count[element] += 1
    
    # copies count array onto array
    i = 0
    for j in range(len(count)):
        for _ in range(count[j]):
            array[i] = j
            i += 1

def stable_counting_sort(array: list[tuple[int, T]]) -> None:

    # creates array of arrays from index 0 to max element
    max_element = max(array)[0]
    count = [[] for _ in range(max_element + 1)]

    # adds each element to the count array by its key
    for element in array:
        count[element[0]].append(element)

    # copies sorted count array onto array
    i = 0
    for j in range(len(count)):
        for k in range(len(count[j])):
            array[i] = count[j][k]
            i += 1

if __name__ == '__main__':
    array = [3, 4, 1, 5, 2, 6, 10, 9, 7, 8]
    print(f"Before Sort: {array}")
    counting_sort(array)
    print(f"After Sort: {array}")
    