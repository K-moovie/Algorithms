"""
Author: Kim YeongHwa
Date: 2020-07-22
Title: 15650
Language: Python 3
"""

def dfs(depth, start):
    if depth == M:
        print(*arr)
        return

    for i in range(start, N):
        if visited[i]:
            continue
        visited[i] = True
        arr[depth] = num_list[i]
        dfs(depth + 1, i + 1)
        visited[i] = False

N, M = map(int, input().split())
num_list = range(1, N + 1)
visited = [False] * N
arr = [0] * M
dfs(0, 0)

