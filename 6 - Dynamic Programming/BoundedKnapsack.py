"""
    Bounded Knapsack Problem

    Function: Finds maximum value you can take with given capacity and items
    Time Complexity (Worst): O(n*c)
    Space Complexity (Auxiliary): O(n*c)

"""

def bounded_knapsack(items: list[tuple[int, int]], capacity: int) -> int:
    
    # initialises memo array
    memo = [[] for _ in range(len(items)+1)]
    for i in range(len(memo)):
        memo[i] = [0 for _ in range(capacity+1)]
    
    # finds memo[i][c] which contains the solution of knapsack for items[0...i-1] and capacity c, for each i and c
    for i in range(1, len(items)+1):
        for j in range(1, capacity+1):
            excluded_value = memo[i-1][j]
            included_value = 0
            if items[i-1][0] <= j:
                included_value = items[i-1][1] + memo[i-1][j-items[i-1][0]]
            memo[i][j] = max(excluded_value, included_value)

    # returns the max value for given capacity and items
    return memo[len(items)][capacity]

if __name__ == '__main__':
    items = [(6, 230), (1, 40), (5, 350), (9, 550)]
    print(f"Items: {items}")
    capacity = 12
    print(f"Max Value with a Capacity of {capacity} = {bounded_knapsack(items, capacity)}")
