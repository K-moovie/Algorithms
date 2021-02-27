"""
Author: Kim YeongHwa
Date: 2021-02-27
Title: Programmers/Summer-Winter Coding(2018)/스킬 트리
Language: Python 3
"""

def check_skill_array(consistance_array):
    for i in range(len(consistance_array)):
        if i is not consistance_array[i]:
            return False
    return True


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_array = []
        for item in skill_tree:

            # skill_tree의 i번 째 item이 skill에  존재할 떄
            if item in skill:
                skill_array.append(skill.index(item))
        if check_skill_array(skill_array):
            answer = answer + 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
result = solution(skill, skill_trees)
print(result)