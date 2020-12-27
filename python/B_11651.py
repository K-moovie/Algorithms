"""
Author: Kim YeongHwa
Date: 2020-07-19
Title: 11651
Language: Python 3
"""

N = int(input())
matrix = [[] for i in range(200001)]
for i in range(0, N):
    x, y = map(int, input().split())
    matrix[y].append(x)

for i in range(-100000, 100001):
    if matrix[i]:
        matrix[i].sort()
        for j in range(0, len(matrix[i])):
            print(str(matrix[i][j]) + " " + str(i))