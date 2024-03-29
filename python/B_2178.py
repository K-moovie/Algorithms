"""
Author: Kim YeongHwa
Date: 2021-10-02
Title: BAEKJOON/2178/미로 탐색
Language: Python 3
Contents:
    N×M크기의 배열로 표현되는 미로가 있다.
    1	0	1	1	1	1
    1	0	1	0	1	0
    1	0	1	0	1	1
    1	1	1	0	1	1
    미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
    이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
    한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
    위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
Input:
4 6
110110
110110
111111
111101

Output:
9
"""
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        cur_x, cur_y = queue.popleft()

        if cur_x == N - 1 and cur_y == M - 1:
            return visited[N -1][M-1]
        for i in range(4):
            go_x = cur_x + dir_x[i]
            go_y = cur_y + dir_y[i]

            if go_x < 0 or go_x > N - 1:
                continue
            elif go_y < 0 or go_y > M - 1:
                continue
            elif maze[go_x][go_y] == 0:
                continue
            elif visited[go_x][go_y] > 0:
                continue

            visited[go_x][go_y] = visited[cur_x][cur_y] + 1
            queue.append((go_x, go_y))
            # print(cur_x, cur_y, queue)


print(bfs(0, 0))
