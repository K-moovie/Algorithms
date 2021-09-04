"""
Author: Kim YeongHwa
Date: 2021-08- 22
Title: Programmers/2018 KAKAO BLIND RECRUITMENT/뉴스 클러스터링
Language: Python 3
Contents:

"""
import re


def solution(str1, str2):
    answer = 0
    pattern = re.compile('[a-z]*')

    str1 = ''.join(pattern.findall(str1.lower()))
    str2 = ''.join(pattern.findall(str2.lower()))

    set_a = []
    set_b = []

    print('str1: {}, str2: {}'.format(str1, str2))

    start, end = 0, 2
    len_a = len(str1)
    len_b = len(str2)

    while True:
        if end <= len_a:
            set_a.append(str1[start:end])
        if end <= len_b:
            set_b.append(str2[start:end])
        start = end - 1
        end = start + 2
        if end > len_a and end > len_b:
            break


    print('set_a: {}, set_b: {}'.format(set_a, set_b))


    return answer


if __name__ == '__main__':
    str1 = "abcde"
    str2 = "abcdfege"
    expected = 16384
    result = solution(str1, str2)

    if expected == result:
        print("정답입니다.")
    else:
        print("오답입니다.")
    print('Expected: {0}\nResult: {1} '.format(expected, result))
