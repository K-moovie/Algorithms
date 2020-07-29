"""
Author: Kim YeongHwa
Date: 2020-07-22
Title: 9663
Language: Python 3
"""
import copy

def is_possible(i, j):
    visited_queue.append(copy.deepcopy(visited))
    # print()
    # print(visited_queue)
    for a in range(N):
        for b in range(N):
            if (i == a) or (j == b):
                visited[a][b] = True
            if i + j == a + b:
                visited[a][b] = True
            if i - j + N - 1 == a - b + N - 1:
                visited[a][b] = True

def dfs(depth, x):
    global count
    global visited
    global visited_queue
    if depth == N:
        count += 1
        # print("count: " + str(count))
        return

    for i in range(x, N):
        for j in range(N):
            if visited[i][j]:
                continue
            is_possible(i, j)
            # print("depth: " + str(depth))
            # print(i, j)
            # print(visited)

            dfs(depth + 1, i + 1)
            visited = copy.deepcopy(visited_queue.pop())
count = 0

N = int(input())
visited = [[False] * N for _ in range((int(N)))]
visited_queue = []

dfs(0, 0)
print(count)

# N = int(input())
# count = 0
# row, diagonal_line_right, diagonal_line_left = [False] * N, [False] * (2 * N - 1), [False] * (2 * N - 1)
#
#
# def dfs(i):
#     global count
#     if i == N:
#         count += 1
#         return
#     for j in range(N):
#         if not (row[j] or diagonal_line_right[i + j] or diagonal_line_left[i - j + N - 1]):
#             row[j] = diagonal_line_right[i + j] = diagonal_line_left[i - j + N - 1] = True
#             dfs(i + 1)
#             row[j] = diagonal_line_right[i + j] = diagonal_line_left[i - j + N - 1] = False
#
# dfs(0)
# print(count)
