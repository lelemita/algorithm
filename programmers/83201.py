# Weekly Challenge: 2nd week
# https://programmers.co.kr/learn/courses/30/lessons/83201?language=python3
# 첫시도 실패 케이스: 10, 12, 15, 16, 19 - 중복여부를 잘못 적용하고 있었음
# 두번째 시도: 통과
# 세번째 시도: 개선 transpose, labeling (윤응구님 풀이 참고)
## 윤응구님의 풀이
## solution = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)], map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1], ((s[i], s[:i] + s[i+1:]) for i, s in enumerate(zip(*scores))))))


def solution(scores):
    answer = ''
    scores = zip(*scores)
    for idx, scos in enumerate(scores):
        mini, maxi, total, is_once = calculate(scos, idx)
        people = len(scos)
        self = scos[idx]
        if is_once and self in (mini, maxi):
            total -= self
            people -= 1
        answer += "FDDCBAA"[max(0, int(total/people/10)-4)]
    return answer


def calculate(scos, idx):
    total = 0
    mini = 101
    maxi = -1
    is_once = True
    for i, sco in enumerate(scos):
        total += sco
        if mini > sco:
            mini = sco
        if maxi < sco:
            maxi = sco
        if i != idx and sco == scos[idx]:
            is_once = False
    return mini, maxi, total, is_once


if __name__ == "__main__":
    assert solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
                     [24, 90, 94, 75, 65]]) == "FBABD"
    assert solution([[50, 90], [50, 87]]) == "DA"
    assert solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]) == "CFD"
    assert solution([[75, 50, 100], [75, 100, 20], [100, 100, 20]]) == "BBF"
    print("done")
