"""
Author: Kim YeongHwa
Date: 2020-08-07
Title: 1003
Language: Python 3
"""

def fibonacci(n):
    for i in range(n - 1):
        fibonacci_array.append(fibonacci_array[i] + fibonacci_array[i + 1])

N = int(input())
fibonacci_array = [0, 1]
fibonacci(40)
user_input = []
for _ in range(N):
    user_input.append(int(input()))

for i in range(N):

    if user_input[i] > 1:
        print(str(fibonacci_array[user_input[i] - 1])  + str(" ") +  str(fibonacci_array[user_input[i]]))
    elif user_input[i] == 1:
        print(str("0 1"))
    elif user_input[i] == 0:
        print(str("1 0"))