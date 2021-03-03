"""
Author: Kim YeongHwa
Date: 2021-03-04
Title: Programmers/KAKAO BLIND RECRUITMENT/신규 아이디 추천
Language: Python 3
"""

import re

def solution(new_id):
    answer = ''
    # 1 대문자를 소문자로
    answer = new_id.lower()

    # 2 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    p = re.compile('[a-z0-9|\-|_|.]+')
    answer = p.findall(answer)
    answer = "".join(answer)

    # 3 ..을 .으로 치환
    for char in answer:
        answer = re.sub('\.{2}', '.', answer)
    answer = "".join(answer)

    # 4 .가 문장의 처음이나 끝에 존재한다면 제거
    answer = re.sub('^\.', '', answer)
    answer = re.sub('\.$', '', answer)

    # 5 빈 문자열이면 a를 대입
    if not answer:
        answer = 'a'

    # 6 문자열의 길이가 16이상이면 15개의 문자까지 남기기, #4 고려하기
    if len(answer) > 15:
        answer = answer[:15]
        answer = re.sub('\.$', '', answer)

    # 7 문자열의 길이가 2자 이하라면 마지막 문자를 반복하여 길이가 3이 되도록 구성
    while True:
        if len(answer) > 2:
            break
        answer += answer[-1]

    return answer

new_id = 'abcdefghijklmn.p'
result = solution(new_id)
print(result)