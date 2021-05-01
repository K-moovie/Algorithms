import bisect
import collections
import itertools



di = collections.defaultdict(lambda:20)

print(di['a'])

result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect([60, 70, 80, 90], score)  # 점수가 정렬되어 삽입될 수 있는 포지션을 반환
    grade = 'FDCBA'[pos]
    result.append(grade)

print(list(map(''.join, itertools.combinations(result, 2))))
l = dict(collections.Counter(result))
print(l['F'])
print(l)
deque = collections.deque(result)
print(deque.popleft())
print(deque.pop())
# print(result)