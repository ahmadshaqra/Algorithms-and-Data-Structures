"""
    Partition

    Function: Partitions a list of integers (unstable)
    Time Complexity (Worst): O(n)
    Space Complexity (Auxiliary): O(1)

"""

def partition(array: list[int], start: int = None, end: int = None, pivot : int = None) -> int:
    
    # checks if start and end index have been inputted
    if start == None or end == None:
        start = 0
        end = len(array) - 1
    
    # checks if pivot has been inputted
    if pivot == None:

        # sets pivot to first element
        pivot = array[start]
    else:

        # swaps pivot with first element
        pivot_index = array.index(pivot)
        array[pivot_index], array[start] = array[start], array[pivot_index]

    # sets up pointers
    left = start + 1
    right = end

    # loops until left and right cross
    while left <= right:

        # moves left to right until it finds an element larger than the pivot
        while left <= right and array[left] <= pivot:
            left += 1
        
        # moves right to left until it finds an element smaller than or equal to the pivot
        while left <= right and array[right] > pivot:
            right -= 1
        
        # swaps elements at left and right if they haven't crossed
        if left <= right:
            array[left], array[right] = array[right], array[left]

    # swaps element at right with pivot
    array[right], array[start] = array[start], array[right]
    
    # returns pivot position after partitioning
    return right

if __name__ == '__main__':
    array = [3, 4, 1, 5, 2, 6, 10, 9, 7, 8]
    print(f"Before Partition: {array}")
    pivot = partition(array, None, None, 5)
    print(f"After Partition (Pivot = {array[pivot]}): {array}")
    