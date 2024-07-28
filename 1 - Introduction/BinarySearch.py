"""
    Binary Search

    Function: Finds an element in a sorted list
    Time Complexity (Worst): O(log(n)) 
    Space Complexity (Auxiliary): O(1)

"""

def binary_search(array: list[int], key: int) -> int | None:

    # initialise lo and hi pointers
    lo = 0
    hi = len(array)

    # checks list dividing search in half each time
    while (lo <= hi):

        # sets mid pointer to middle of list
        mid = (lo + hi) // 2

        # checks where key is relative to mid and changes pointers accordingly
        if key == array[mid]:
            return mid
        elif key > array[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 5
    print(f"Key ({key}) is in index position: {binary_search(array, key)}")
    