"""
Author: Kim YeongHwa
Date: 2021-08-19
Title: Baekjoon/1086/부분합
Language: Python 3
Contents:
    문제
    10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
    이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

    입력
    첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다.
    둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

    출력
    첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

    예제 입력 1
    10 15
    5 1 3 5 10 7 4 9 2 8

    예제 출력 1
    2
"""
import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
tmp_sum = 0
min_length = sys.maxsize

while right <= N:
    # print('left: {}, right: {}, sum: {}, min: {}'.format(left, right, tmp_sum, min_length))
    if tmp_sum >= S:
        min_length = min(right - left, min_length)
        tmp_sum -= arr[left]
        left += 1
    else:
        if right == N:
            break
        tmp_sum += arr[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)