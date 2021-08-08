import math

def solution(lines):
    answer = 0
    starts = []
    ends = []
    for line in lines:
        h = float(line[11:13])
        m = float(line[14:16])
        s = float(line[17:19])
        ms = float(line[20:23])
        t = (float(line[24: -1]) - math.floor(float(line[24: -1]))) * 1000 + math.floor(float(line[24: -1])) * 1000
        end_time = (((((h * 60) + m) * 60) + s) * 1000) + ms
        start_time = end_time - (t - 1)
    return answer

solution(["2016-09-15 03:10:33.020 0.011s", "2016-09-15 01:00:07.000 0.14s"])