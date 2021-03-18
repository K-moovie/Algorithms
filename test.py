from itertools import cycle


def solution(answers):
    answer = []
    m_1 = cycle([1, 2, 3, 4, 5])
    m_2 = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    m_3 = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    score = [0, 0, 0]

    for i in range(len(answers)):
        score[0] += [4, 2][next(m_2) == answers[i]]
        print(score)
        score[1] += [0, 1][next(m_2) == answers[i]]
        score[2] += [0, 1][next(m_3) == answers[i]]

    for i in range(3):
        if score[i] == max(score):
            answer.append(i + 1)

    return answer

if __name__ == '__main__':
    answer = [1, 2, 3, 4, 7, 9]
    result = solution(answer)