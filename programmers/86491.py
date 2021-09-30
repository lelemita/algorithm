# 코딩테스트 연습 > 위클리 챌린지 > 8주차
# https://programmers.co.kr/learn/courses/30/lessons/86491
# 뭐지... 왜 난이도 갑자기 훅 떨어졌을까....

def solution(sizes):
    x = y = 0
    for arr in sizes:
        if arr[0] < arr[1]:
            x = max(x, arr[0])
            y = max(y, arr[1])
        else:
            x = max(x, arr[1])
            y = max(y, arr[0])
    return x * y


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]), 4000)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]), 120)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]), 133)
