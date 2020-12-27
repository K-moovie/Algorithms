"""
Author: Kim YeongHwa
Date: 2020-07-08
Title: 1436
Language: Python 3
"""

input = int(input())
target = "666"

count = 0
i = 0

while True:
    i += 1
    if str(i).find(target) >= 0:
        count += 1
    if count == input:
        print(i)
        break