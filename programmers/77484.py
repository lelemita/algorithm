# 코딩테스트 연습 > 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 로또의 최고 순위와 최저 순위
# 오늘은 너무 피곤해서 Lv.1

def solution(lottos, win_nums):
    answer = [1, 6]
    cnt_right = 0
    cnt_zero = 0
    for num in lottos:
        if num == 0:
            cnt_zero += 1
        elif num in win_nums:
            cnt_right += 1
    answer[0] = min(7 - (cnt_right + cnt_zero), 6)
    answer[1] = min(7 - cnt_right, 6)
    return answer


if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]), [3, 5])
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]), [1, 6])
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]), [1, 1])
    print(solution([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]), [6, 6])
