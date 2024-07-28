"""
    Merge Sort

    Function: Sorts list of integers (stable)
    Time Complexity (Worst): O(n*log(n))
    Space Complexity (Auxiliary): O(n)

"""

def merge_sort(array: list[int]) -> None:

    if len(array) > 1:

        # splits array in half
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # sorts left and right half recursively
        merge_sort(left)
        merge_sort(right)

        # merges left and right side of array
        merge(array, left, right)
    
def merge(array: list[int], left: list[int], right: list[int]) -> None:
    
    # sets the array index (k) and the left and right index (i and j) to 0
    i = j = k = 0

    # merges left and right array until one is empty
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # adds whatever is left
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

if __name__ == '__main__':
    array = [3, 4, 1, 5, 2, 6, 10, 9, 7, 8]
    print(f"Before Sort: {array}")
    merge_sort(array)
    print(f"After Sort: {array}")
    