def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]
            answer.append(sum)

    # 집합 자료형을 사용한 중복 값 제거.
    set_answer = set(answer)
    answer = list(set_answer)
    answer = sort(answer)
    return answer

# Selection Sort (선택정렬)
def sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            # 최소값 index 찾기
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

numbers = [2,1, 3,4,1]
result = solution(numbers)
print(result)