"""
    Selection Sort

    Function: Sorts list of integers (unstable)
    Time Complexity (Worst): O(n^2)
    Space Complexity (Auxiliary): O(1)

"""

def selection_sort(array: list[int]) -> None:

    # traverses through all elements in array
    for i in range(len(array)):

        # finds index of min element in unsorted section
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        # swaps the min element with first element in unsorted section
        array[i], array[min_index] = array[min_index], array[i]

if __name__ == '__main__':
    array = [3, 4, 1, 5, 2, 6, 10, 9, 7, 8]
    print(f"Before Sort: {array}")
    selection_sort(array)
    print(f"After Sort: {array}")
    