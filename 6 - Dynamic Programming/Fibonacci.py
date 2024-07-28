"""
    Fibonacci with Memoization

    Function: Finds and returns the nth fibonacci number
    Time Complexity (Worst): O(n)
    Space Complexity (Auxiliary): O(n)

"""

def fibonacci_top_down(n: int, memo: list[int] = None) -> int:

    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # initialises memo array
    if memo == None:
        memo = [None for _ in range(n+1)]
        memo[0] = 0
        memo[1] = 1

    # finds nth fibonacci number and returns answer
    memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)
    return memo[n]

def fibonacci_bottom_up(n: int) -> int:

    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # initialises memo array
    memo = [None for _ in range(n+1)]
    memo[0] = 0
    memo[1] = 1

    # finds nth fibonacci number and returns answer
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

if __name__ == '__main__':
    n = 15
    print(f"{n}th Fibonacci Number = {fibonacci_top_down(n)}")
    n = 20
    print(f"{n}th Fibonacci Number = {fibonacci_bottom_up(n)}")
    