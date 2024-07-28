"""
    Karatsuba's Algorithm

    Function: Multiplies two integers together
    Time Complexity (Worst): O(n^log(3))
    Space Complexity (Auxiliary): O(n) 

"""

from math import ceil

def karatsuba(x: int, y: int) -> int:
    
    # gets digits of each integer
    x_digits = len(str(x))
    y_digits = len(str(y))

    # if either integer has 1 digit, it returns the product of the digits
    if x_digits == 1 or y_digits == 1:
        return x * y
    else:

        # finds the max number of digits
        n = ceil(max(x_digits, y_digits) / 2)

        # calculates the most and least significant digits of x and y
        x_m = x // 10**n
        x_l = x % 10**n
        y_m = y // 10**n
        y_l = y % 10**n

        # makes the three recursive calls and finds all three terms
        a = karatsuba(x_m, y_m)
        b = karatsuba(x_l, y_l)
        c = karatsuba(x_m + x_l, y_m + y_l) - a - b

        # calculates and returns result
        return (a * 10**(2*n)) + (c * 10**n) + b

if __name__ == '__main__':
    x = 420
    y = 690
    print(f"{x} x {y} = {karatsuba(x, y)}")
    