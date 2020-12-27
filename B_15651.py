"""
Author: Kim YeongHwa
Date: 2020-07-22
Title: 15651
Language: Python 3
"""

def dfs(depth):
    if depth == M:
        print(*arr)
        return

    for i in range(N):
        arr[depth] = num_list[i]
        dfs(depth + 1)

N, M = map(int, input().split())
num_list = range(1, N + 1)
visited = [False] * N
arr = [0] * M

dfs(0)