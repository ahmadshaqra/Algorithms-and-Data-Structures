"""
    Bubble Sort

    Function: Sorts list of integers (stable)
    Time Complexity (Worst): O(n^2)
    Space Complexity (Auxiliary): O(1)

"""

def bubble_sort(array: list[int]) -> None:

    # traverses through all elements in array
    for i in range(len(array)):

        # traverses through all elements in unsorted section
        for j in range(len(array)-i-1):

            # swaps if current index is larger than next index
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

if __name__ == '__main__':
    array = [3, 4, 1, 5, 2, 6, 10, 9, 7, 8]
    print(f"Before Sort: {array}")
    bubble_sort(array)
    print(f"After Sort: {array}")
    