"""
    Radix Sort

    Function: Sorts list of integers (stable)
    Time Complexity (Worst): O(n*k)
    Space Complexity (Auxiliary): O(n+k)

"""

from CountingSort import stable_counting_sort
from typing import TypeVar
T = TypeVar('T')

def radix_sort(array: list[int]) -> None:

    # finds number of digits of max number in array
    digits = len(str(max(array)))

    # uses stable counting sort on each nth digit
    for i in range(digits):
        indexing(array, i)
        stable_counting_sort(array)
    
    # removes keys from array
    for i in range(len(array)):
        array[i] = array[i][1]

def indexing(array: list[tuple[int, T]], n: int) -> None:

    # adds keys to array using nth digit
    if n == 0:
        for i in range(len(array)):
            digit = array[i] % 10
            array[i] = (digit, array[i])
    else:
        for i in range(len(array)):
            digit = (array[i][1] // 10**n) % 10
            array[i] = (digit, array[i][1])

if __name__ == '__main__':
    array = [8565, 7620, 8747, 7727, 3244, 8016, 8604, 3162, 6028, 4759]
    print(f"Before Sort: {array}")
    radix_sort(array)
    print(f"After Sort: {array}")
    