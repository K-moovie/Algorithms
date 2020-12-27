"""
Author: Kim YeongHwa
Date: 2020-07-14
Title: 10814
Language: Python 3
"""

N = int(input())

array = [[] for i in range(201)]
for i in range(0, N):
    age, name = map(str, input().split())
    array[int(age)].append(name)

for i in range(0, 201):
    if array[i]:
        for j in range(0, len(array[i])):
            print(str(i) + " " + array[i][j])