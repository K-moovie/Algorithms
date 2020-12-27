"""
Author: Kim YeongHwa
Date: 2020-08-07
Title: 2748
Language: Python 3
"""

# recursive
"""def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n - 1)

N = int(input())
print(fibonacci(N))"""


def fibonacci(n):
    first = 0
    second = 1
    if n == first:
        return first
    elif n == second:
        return second
    else:
        result = 0
        for i in range(2, n + 1):
            result = first + second
            first = second
            second = result
        return result

N = int(input())
print(fibonacci(N))