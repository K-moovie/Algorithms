from bisect import bisect_left
from collections import defaultdict


def solution(n, t, m, timetable):
    answer = ''
    times = list()
    for i in range(n):
        time = i * t
        min = str(time % 60)
        hour = str(9 + (time // 60))
        if len(min) == 1:
            min = '0' + min
        if len(hour) == 1:
            hour = '0' + hour
        times.append('{0}:{1}'.format(hour, min))
    # print(times)

    dic = defaultdict(list)
    for time in times:
        dic[time]

    for time in timetable:
        pos = bisect_left(times, time)
        while True:
            if len(dic[times[pos]]) < m:
                break
            else:
                pos += 1
        dic[times[pos]].append(time)

    for i, time in enumerate(times[::-1]):
        if len(dic[time]) < m:
            hour = time[0:2]
            min = time[3:5]
            print(time)
        # if i == len(times) - 1:
        #     print(dic[time])
    print(dic)

    return answer

if __name__ == '__main__':
    # n = 2
    # t = 10
    # m = 2
    # timetable = ["09:10", "09:09", "08:00"]

    # n = 1
    # t = 1
    # m = 5
    # timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]

    n = 2
    t = 1
    m = 2
    timetable = ["09:00", "09:00", "09:00", "09:00"]
    solution(n, t, m, timetable)