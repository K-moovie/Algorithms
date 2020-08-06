"""
Author: Kim YeongHwa
Date: 2020-08-06
Title: 14889
Language: Python 3
"""
import copy
import math

def dfs(depth, start):
    if depth == int(N/2):
        start_result = 0
        link_result = 0
        start = copy.deepcopy(temp)
        link = [i for i in range(N) if i not in start]

        for i in start:
            for j in start:
                start_result += ability_array[i][j]

        for i in link:
            for j in link:
                link_result += ability_array[i][j]
        result.append(abs(start_result - link_result))
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            temp.append(i)

            dfs(depth + 1, i)

            visited[i] = False
            temp.remove(i)


N = int(input())
# 2차원 배열 입력
ability_array = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
temp = []
result = []
dfs(0, 0)

print(min(result))
# start = result[:int(len(result)/2)]
# link = result[int(len(result)/2):]
# link.reverse()
#
# print(*start)
# print()
# print(*link)