import itertools
import re
import copy

def solution(expression):
    answer = 0
    split = []
    priorities = list()
    temp = ''
    p = re.compile('[*|+|-]')
    length = len(expression) - 1
    result = list()
    for index, char in enumerate(expression):
        if re.match(p, char):
            priorities.append(char)
            split.append(temp)
            temp = ''
            split.append(char)
        else:
            temp += char
        if index == length:
            split.append(temp)
    priorities = set(priorities)
    priorities = list(itertools.permutations(priorities, len(priorities)))
    print(priorities)
    for priority in priorities:
        result.append(cal(split, priority))
    answer = max(result)
    return answer

def cal(expr: str, priority: str):
    expr = copy.deepcopy(expr)
    result = 0
    print(priority)
    for op in priority:
        for _ in range(expr.count(op)):
            index = expr.index(op)
            left = expr[index - 1]
            right = expr[index + 1]
            if op == '-':
                temp = int(left) - int(right)
            elif op == '+':
                temp = int(left) + int(right)
            elif op == '*':
                temp = int(left) * int(right)
            result = expr[index - 1] = str(temp)
            expr.pop(index)
            expr.pop(index)
    return abs(int(result))

if __name__ == '__main__':
    solution("50*6-3*2")