"""
Author: Kim YeongHwa
Date: 2021-05-01
Title: Programmers/연습문제/124 나라의 숫자
Language: Python 3
Contents:
    문제 설명
    124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

    124 나라에는 자연수만 존재합니다.
    124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
    예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

    10진법	124 나라	10진법	124 나라
    1	1	6	14
    2	2	7	21
    3	4	8	22
    4	11	9	24
    5	12	10	41
    자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

    제한사항
    n은 500,000,000이하의 자연수 입니다.

    입출력 예
    n	result
    1	1
    2	2
    3	4
    4	11
"""


import itertools
import bisect

def solution(n):
    global result
    result= list()
    answer = ''
    numbers = [0, 3]
    item = 3
    while True:
        sum = numbers[-1]
        item *= 3
        if n < item:
            break
        numbers.append(sum + item)

    pos = bisect.bisect_left(numbers, n)
    make_number(pos, '')

    index = n - numbers[pos - 1]
    answer = result[index - 1]
    return answer

def make_number(depth, item):
    global result
    if len(item) == depth:
        result.append(item)
        return

    make_number(depth, item+'1')
    make_number(depth, item+'2')
    make_number(depth, item+'4')

# 효율성 테스트를 생각한 코드
# def solution(n):
#     if n <= 3:
#         return '124'[n - 1]
#     else:
#         q, r = divmod(n - 1, 3)
#         return solution(q) + '124'[r]

if __name__ == '__main__':
    print('Expected: {0}\nResult: 122'.format(solution(17)))