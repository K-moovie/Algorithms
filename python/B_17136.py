"""
Author: Kim YeongHwa
Date: 2021-12-27
Title: BAEKJOON/17136/색종이 붙이기
Language: Python 3
Contents:
    <그림 1>과 같이 정사각형 모양을 한 다섯 종류의 색종이가 있다. 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.
    색종이를 크기가 10×10인 종이 위에 붙이려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다. 1이 적힌 칸은 모두 색종이로 덮여져야 한다. 색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다. 또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.
    종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자.

Input:
0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 1 1 1 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

Output:
7
"""
import sys

sys.setrecursionlimit(10000000)
input = sys.stdin.readline


def dfs(y, x, count):
    global answer, used

    if y >= 10:
        answer = min(answer, count)
        return

    if x >= 10:
        dfs(y + 1, 0, count)
        return

    # 현재 좌표가 1일 때
    # 색종이 붙이기
    if paper[y][x] == 1:
        for k in range(5):
            if used[k] == 5:
                continue
            if y + k >= 10 or x + k >= 10:
                continue

            flag = True
            for i in range(y, y + k + 1):
                for j in range(x, x + k + 1):
                    if paper[i][j] == 0:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                for i in range(y, y + k + 1):
                    for j in range(x, x + k + 1):
                        paper[i][j] = 0
                used[k] += 1
                dfs(y, x + k + 1, count + 1)

                used[k] -= 1
                for i in range(y, y + k + 1):
                    for j in range(x, x + k + 1):
                        paper[i][j] = 1
    # 현재 좌표가 0이라면
    # 옆으로 넘어간다.
    else:
        dfs(y, x + 1, count)


paper = [list(map(int, input().split())) for _ in range(10)]
used = [0] * 5
answer = 26

dfs(0, 0, 0)
print(answer if answer != 26 else -1)
