"""
Author: Kim YeongHwa
Date: 2020-07-18
Title: 11650
Language: Python 3
"""

N = int(input())
matrix = [[] for i in range(200001)]
for i in range(0, N):
    x, y = map(int, input().split())
    matrix[x].append(y)

for i in range(-100000, 100001):
    if matrix[i]:
        matrix[i].sort()
        for j in range(0, len(matrix[i])):
            print(str(i) + " " +str(matrix[i][j]))
