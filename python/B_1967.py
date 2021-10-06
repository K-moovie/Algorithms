"""
Author: Kim YeongHwa
Date: 2021-09-29
Title: BAEKJOON/1967/트리의 지름
Language: Python 3
Contents:
    트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다.
    트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다.
    이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
    이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.
    입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.
    트리의 노드는 1부터 n까지 번호가 매겨져 있다.

Input:
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10

Output:
45
"""
import sys

sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
weight1 = [0 for _ in range(N + 1)]
weight2 = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    parent, child, w = map(int, sys.stdin.readline().split())
    tree[parent].append((child, w))
    tree[child].append((parent, w))


def dfs(current_node, start_node, weight):
    weight[start_node] = 0
    for node, w in tree[current_node]:
        if weight[node] == 0:
            weight[node] = weight[current_node] + w
            dfs(node, start_node, weight)


dfs(1, 1, weight1)

max_index = 0
start_node = 0
for i in range(len(weight1)):
    if max_index < weight1[i]:
        max_index = weight1[i]
        start_node = i

dfs(start_node, start_node, weight2)
print(max(weight2))