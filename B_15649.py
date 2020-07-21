"""
Author: Kim YeongHwa
Date: 2020-07-21
Title: 15649
Language: Python 3
"""

def dfs(depth):
    # 주어진 개수만큼 채워지면 출력한다
    if depth == M:
        print(*arr)
        return

    for i in range(0, N):
        if visited[i]:
            continue

        # i번째 탐색하므로 True
        visited[i] = True
        # arr.append(num_list[i])
        arr[depth] = num_list[i]
        # 현재의 i를 기준으로 가지치기 시작
        dfs(depth + 1)
        visited[i] = False


N, M = map(int, input().split())

num_list = range(1, N + 1)
visited = [False] * N
arr = [0] * M

dfs(0)