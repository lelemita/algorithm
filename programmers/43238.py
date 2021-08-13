# 코딩테스트 연습 > 이분탐색 > 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238
# n차 시도: 인원이 맞아도, 최소시간을 더 찾아야 함.
# 참고: https://nsios.tistory.com/115

def solution(n, times):
    answer = 0
    right = min(times) * n
    left = 1
    while left <= right:
        done = 0
        mid = (left + right) // 2
        for ti in times:
            done += mid // ti
            if done >= n:
                right = mid - 1
                answer = mid
                break
        if done < n:
            left = mid + 1
    return answer


if __name__ == "__main__":
    print(solution(6, [7, 10]), 28)
    print(solution(5, [1, 2, 3, 4, 5]), 3)
