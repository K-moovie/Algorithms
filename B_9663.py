"""
Author: Kim YeongHwa
Date: 2020-07-22
Title: 9663
Language: Python 3
"""
import copy

def is_possible(i, j):
    visited_queue.append(copy.deepcopy(visited))
    for a in range(N):
        for b in range(N):
            if (i == a) or (j == b):
                visited[a][b] = True
            if i + j == a + b:
                visited[a][b] = True
            if i - j + N - 1 == a - b + N - 1:
                visited[a][b] = True


def dfs(depth, x, y):
    global count
    global visited
    if depth == N:
        count += 1
        print("count: " + str(count))
        return

    for i in range(x, N):
        for j in range(y, N):
            if visited[i][j]:
                continue
            is_possible(i, j)
            print(i, j)
            # if j == N - 1:
            #     dfs(depth + 1, i + 1, 0)
            #     visited = copy.deepcopy(visited_queue.pop())
            #     print(visited)

            dfs(depth, i, j + 1)
            visited = copy.deepcopy(visited_queue.pop())
            print(visited)
    # check point: 탐색이 불완전함

count = 0

N = int(input())
visited = [[False] * N for _ in range((int(N)))]
visited_queue = []

dfs(0, 0, 0)
print(count)