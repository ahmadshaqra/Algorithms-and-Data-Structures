"""
    Coins Change Problem

    Function: Finds the minimum number of coins needed to get a value
    Time Complexity (Worst): O(c*v)
    Space Complexity (Auxiliary): O(c*v)

"""

def coins_change_top_down(coins: list[int], value: int, min_coins: list[int] = None) -> int:

    # base case
    if value == 0:
        return 0
    
    # initialises memo array
    if min_coins == None:
        min_coins = [None for _ in range(value+1)]
    
    # checks if min coins for given value has been found
    if min_coins[value] == None:
        
        # finds the min coins required to reach given value
        min_coins_required = float("inf")
        for i in range(len(coins)):
            if coins[i] <= value:
                min_coins_required = min(min_coins_required, 1 + coins_change_top_down(coins, value - coins[i], min_coins))
        min_coins[value] = min_coins_required

    # returns min coins for given value
    return min_coins[value]

def coins_change_bottom_up(coins: list[int], value: int) -> int:
    
    # initialises memo array and base case
    min_coins = [float("inf") for _ in range(value+1)]
    min_coins[0] = 0

    # finds the min coins required for each value from 1 to value
    for i in range(1, value+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                min_coins[i] = min(min_coins[i], 1+min_coins[i-coins[j]])
            
    # returns min coins for given value
    return min_coins[value]

if __name__ == '__main__':
    coins = [9, 5, 6, 1]
    print(f"Coin Denominations: {coins}")
    value = 12
    print(f"Minimum Coins Required for {value} = {coins_change_bottom_up(coins, value)}")
    value = 4
    print(f"Minimum Coins Required for {value} = {coins_change_top_down(coins, value)}")
