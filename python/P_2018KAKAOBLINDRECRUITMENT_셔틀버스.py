from bisect import bisect_left
from collections import defaultdict


def solution(n, t, m, timetable):
    answer = ''
    timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    timetable.sort()
    last_time = (60 * 9) + (n - 1) * t

    for i in range(n):
        if len(timetable) < m: return '%02d:%02d' % (last_time // 60, last_time % 60)
        if i == n - 1:
            if timetable[0] <= last_time: last_time = timetable[m - 1] - 1
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        for j in range(m - 1, -1, -1):
            bus_arrive = (60 * 9) + i * t
            if timetable[j] <= bus_arrive:
                del timetable[j]

if __name__ == '__main__':
    n = 2
    t = 10
    m = 2
    timetable = ["09:10", "09:09", "08:00"]
    expected = "09:09"
    # n = 1
    # t = 1
    # m = 5
    # timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]

    # n = 2
    # t = 1
    # m = 2
    # timetable = ["09:00", "09:00", "09:00", "09:00"]

    result = solution(n, t, m, timetable)

    if expected == result:
        print("정답입니다.")
    else:
        print("오답입니다.")
    print('Expected: {0}\nResult: {1} '.format(expected, result))