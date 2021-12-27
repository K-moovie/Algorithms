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

def check(i,j,size,table):
    target = []
    for y in range(size) :
        for x in range(size) :
            yy, xx = i+y, j+x
            if yy < 0 or yy >= 10 or xx < 0 or xx >= 10 :
                return False, []

            if table[yy][xx] == 0 :
                return False, []
            else :
               target.append((yy, xx))

    temp = [[table[y][x] for x in range(10)] for y in range(10)]
    for y,x in target:
        temp[y][x] = 0

    return True, temp

def DFS(table, rest_cnt, papers):
    global result
    if rest_cnt == 0 :
        result = min(result,25 - sum(papers))
        return
    #print(table,rest_cnt,papers)
    for i in range(10):
        for j in range(10):
            if table[i][j] == 1:
                flag = False
                for size in range(1,6):
                    if papers[size] > 0:
                        check_result, temp = check(i,j,size,table)
                        if check_result:
                            papers[size] -= 1
                            DFS(temp,rest_cnt-(size**2),papers)
                            papers[size] += 1
                        flag = True
                if flag:
                    return

table = [list(map(int,sys.stdin.readline().split())) for _ in range(10)]
rest_cnt = 0

for i in range(10):
    for j in range(10):
        if table[i][j] == 1 :
            rest_cnt += 1

papers = [0,5,5,5,5,5]
result = 26


DFS(table, rest_cnt, papers)
if result == 26:
    print(-1)
else:
    print(result)