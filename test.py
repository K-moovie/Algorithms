# from queue import PriorityQueue
#
#
# def solution(priorities, location):
#     answer = 0
#     que = PriorityQueue(maxsize=len(priorities))
#     current_index = 0
#     print_array = []
#     pri_len = len(priorities)
#
#     while True:
#         print(location)
#         item = priorities.pop(0)
#         if len(print_array) == pri_len - 1:
#             print_array.append(item)
#             break
#
#         if item < max(priorities):
#             priorities.append(item)
#             if location == 0:
#                 location = pri_len - 1
#             else:
#                 location = location - 1
#
#         else:
#             print_array.append(item)
#
#         current_index = current_index + 1
#     answer = location + 1
#     print(print_array)
#     return answer
#
# def solution(priorities, location):
#     answer = 0
#     current_index = 0
#
#     while True:
#         if check(priorities):
#             break
#
#         item = priorities.pop(0)
#         if item < max(priorities):
#             priorities.append(item)
#             if location == 0:
#                 location = len(priorities) - 1
#             else:
#                 location = location - 1
#
#         else:
#             priorities.insert(0, item)
#
#         current_index = current_index + 1
#     answer = location + 1
#     return answer
#
#
# def check(priorities):
#     print(priorities)
#     item = priorities[0]
#     for priority in priorities:
#         if item < priority:
#             return False
#         item = priority
#     return True
#
# solution([1, 2, 3, 2], 0 )

queue = [(1, 2), (2, 2)]

while queue:
    print(queue.index((2,2)))