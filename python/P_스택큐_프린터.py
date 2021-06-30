"""
Author: Kim YeongHwa
Date: 2021-03-03
Title: Programmers/스택/큐/프린터
Language: Python 3
"""

def solution(priorities, location):
    answer = 0
    queue = [(v, i) for i, v in enumerate(priorities)]
    print_queue = []
    while queue:
        item = queue.pop(0)

        if not queue:
            print_queue.append(item)
            break

        # 최대값이 아닐 때
        if item[0] < max(queue)[0]:
            queue.append(item)

        # 최대값 일 때
        else:
            print_queue.append(item)

    answer = print_queue.index((priorities[location], location)) + 1
    return answer

priorities = [2, 1, 3, 2]
location = 2
result  = solution(priorities, location)
print(result)