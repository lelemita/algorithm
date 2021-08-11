# Weekly Challenge: 2nd week
# https://programmers.co.kr/learn/courses/30/lessons/83201?language=python3
# 첫시도 실패 케이스: 10, 12, 15, 16, 19

def solution(scores):
    answer = ''
    scores = transpose(scores)
    for idx, scos in enumerate(scores):
        mini, maxi, total = calculate(scos)
        people = len(scos)
        self = scos[idx]
        if self in (mini, maxi):
            total -= self
            people -= 1
        answer += labeling(total / people)
    return answer


def transpose(arrs):
    result = [[0 for _ in range(len(arrs))] for _ in range(len(arrs[0]))]
    for idx, arr in enumerate(arrs):
        for jdx in range(len(arr)):
            result[jdx][idx] = arr[jdx]
    return result


def calculate(scos):
    total = 0
    mini = 101
    maxi = -1
    for sco in scos:
        total += sco
        if mini > sco:
            mini = sco
        if maxi < sco:
            maxi = sco
    return mini, maxi, total


def labeling(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    # assert solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
    #                  [24, 90, 94, 75, 65]]) == "FBABD"
    # assert solution([[50, 90], [50, 87]]) == "DA"
    # assert solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]) == "CFD"
    print(solution([[100, 100, 0], [0, 100, 100], [100, 0, 100]]))
    print("done")
