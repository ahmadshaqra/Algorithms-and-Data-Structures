"""
    Unbounded Knapsack Problem

    Function: Finds maximum value you can take with given capacity and items
    Time Complexity (Worst): O(n*c)
    Space Complexity (Auxiliary): O(n+c)

"""

def unbounded_knapsack_top_down(items: list[tuple[int, int]], capacity: int, memo: list[int] = None) -> int:

    # initialises memo array and base case
    if memo == None:
        memo = [-1 for _ in range(capacity+1)]
        memo[0] = 0
    
    # checks if max value for given capacity has been found
    if memo[capacity] == -1:

        # finds the max value for given capacity
        max_value = 0
        for item in items:
            if item[0] <= capacity:
                this_value = item[1] + unbounded_knapsack_top_down(items, capacity - item[0], memo)
                if this_value > max_value:
                    max_value = this_value
        memo[capacity] = max_value
    
    # returns the max value for given capacity
    return memo[capacity]

def unbounded_knapsack_bottom_up(items: list[tuple[int, int]], capacity: int) -> int:

    # initialises memo array
    memo = [0 for _ in range(capacity+1)]

    # finds the max value for each capacity from 1 to capacity
    for i in range(1, capacity+1):
        max_value = 0
        for item in items:
            if item[0] <= i:
                this_value = item[1] + memo[i - item[0]]
                if this_value > max_value:
                    max_value = this_value
        memo[i] = max_value

    # returns the max value for given capacity
    return memo[capacity]

if __name__ == '__main__':
    items = [(9, 550), (5, 350), (6, 180), (1, 40)]
    print(f"Items: {items}")
    capacity = 12
    print(f"Max Value with a Capacity of {capacity} = {unbounded_knapsack_top_down(items, capacity)}")
    capacity = 10
    print(f"Max Value with a Capacity of {capacity} = {unbounded_knapsack_bottom_up(items, capacity)}")
