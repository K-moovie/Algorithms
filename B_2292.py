"""
Author: Kim YeongHwa
Date: 2020-07-06
Title: 2292
Language: Python 3
"""

input = int(input())
count = 0
a = 0
b = 1
while True:
    count += 1
    if a <= input <= b:
        break
    else:
        a = b + 1
        b += (6 * count)
print(count)