"""
Author: Kim YeongHwa
Date: 2020-07-22
Title: 9663
Language: Python 3
"""

def is_possible(i, j):
    for a in range(N):
        for b in range(N):
            if (i == a) or (j == b):
                visited[a][b] = False
            if i + j == a + b:
                visited[a][b] = False
            if i - j + N  -1 == a - b + N -1:
                visited[a][b] = False
    print(visited)


def dfs(depth, start):
    if depth == M:
        print(*arr)
        return

    for i in range(start, N):
        arr[depth] = num_list[i]
        dfs(depth + 1, i)

N = int(input())
visited = [[True] * N for _ in range((int(N)))]

is_possible(1, 2)