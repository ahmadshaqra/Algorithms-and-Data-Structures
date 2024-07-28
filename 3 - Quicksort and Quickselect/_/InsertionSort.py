"""
    Insertion Sort

    Function: Sorts list of integers (stable)
    Time Complexity (Worst): O(n^2)
    Space Complexity (Auxiliary): O(1)

"""

def insertion_sort(array: list[int]) -> None:

    # traverses through all elements in array
    for i in range(1, len(array)):
        j = i

        # traverses through sorted section until next element is in correct position
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

if __name__ == '__main__':
    array = [3, 4, 1, 5, 2, 6, 10, 9, 7, 8]
    print(f"Before Sort: {array}")
    insertion_sort(array)
    print(f"After Sort: {array}")
    