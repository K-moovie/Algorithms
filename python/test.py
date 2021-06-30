from collections import deque
from bisect import bisect

bi = bisect([1, 2, 3, 9, 12, 10], 13)
print(bi)