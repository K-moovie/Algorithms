"""
Author: Kim YeongHwa
Date: 2021-09-13
Title: BAEKJOON/11723번/집합
Language: Python 3
Contents:
    비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

    add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    all: S를 {1, 2, ..., 20} 으로 바꾼다.
    empty: S를 공집합으로 바꾼다
Input:
    26
    add 1
    add 2
    check 1
    check 2
    check 3
    remove 2
    check 1
    check 2
    toggle 3
    check 1
    check 2
    check 3
    check 4
    all
    check 10
    check 20
    toggle 10
    remove 20
    check 10
    check 20
    empty
    check 1
    toggle 1
    check 1
    toggle 1
    check 1

Output:
    1
    1
    0
    1
    0
    1
    0
    1
    0
    1
    1
    0
    0
    0
    1
    0
"""

import sys
M = int(input())
s = 0
for _ in range(M):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:
        param = int(cmd[1])

    if cmd[0] == 'all':
        s = (1 << 21) - 1
    elif cmd[0] == 'empty':
        s = 0
    elif cmd[0] == 'add':
        s |= (1 << param)
    elif cmd[0] == 'remove':
        s &= ~(1 << param)
    elif cmd[0] == 'check':
        print(1 if '1' in bin(s & (1 << param)) else 0)
    elif cmd[0] == 'toggle':
        if '1' in bin(s & (1 << param)):
            s &= ~(1 << param)
        else:
            s |= (1 << param)