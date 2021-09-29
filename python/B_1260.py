"""
Author: Kim YeongHwa
Date: 2021-09-29
Title: BAEKJOON/1260/DFS와 BFS
Language: Python 3
Contents:
    그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
    단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
    더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
Input:
5 5 3
5 4
5 2
1 2
3 4
3 1

Output:
3 1 2 5 4
3 1 4 2 5
"""

from sys import stdin
from collections import defaultdict
from collections import deque

n, m, v = map(int, stdin.readline().split())
matrix = defaultdict(list)

for _ in range(m):
    v1, v2 = map(int, stdin.readline().split())
    matrix[v1].append(v2)
    matrix[v2].append(v1)

for key, values in matrix.items():
    matrix[key] = sorted(values)


def dfs(root, visited=[]):
    print('{} '.format(root), end='')
    visited.append(root)
    for vertex in matrix[root]:
        if vertex in visited:
            continue
        dfs(vertex)


def bfs(root):
    queue = deque()
    visited = [root]
    queue.append(root)

    while queue:
        current_vertex = queue.popleft()
        print('{} '.format(current_vertex), end='')
        visited.append(current_vertex)
        for vertex in matrix[current_vertex]:
            if vertex in visited:
                continue
            visited.append(vertex)
            queue.append(vertex)


dfs(v)
print()
bfs(v)
