"""
Author: Kim YeongHwa
Date: 2020-06-30
Title: 2446
Language: Python 3
"""

input = int(input())
max = input*2-1

j = 0
space = 0
for i in range(0, max):
    if i < input:
        space = max - (max - j)
        print(" "*int(space/2) + "*"*(max - j))
    else:
        space = max - (abs(max - j) + 2)
        print(" " * int(space/2) + "*" * (abs(max - j) + 2))
    j += 2
