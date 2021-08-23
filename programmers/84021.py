# not solved yet
# Weekly Challenge: 3rd week
# https://programmers.co.kr/learn/courses/30/lessons/84021
def solution(game_board, table):
    answer = -1
    # 반복: 보드에서 도형 하나 고름
    shape = pick_shape(game_board)
    print(shape)
    # 테이블 4방향 회전
    # # 방향마다 도형 수색
    # # 도형찾으면 answer+= 하고, 테이블에서 도형 없애고, 회전 종료
    return answer


# 해당 도형만 1이고 나머지 0인 배열 만들기
def pick_shape(board):
    shape = [[0 for _ in row] for row in board]
    # 도형 시작점 찾기
    a, b = find_start(board)
    # 도형 표시하기
    for i in range(a, len(board)):
        row = board[i]
        for j in range(len(row)):
            print("while")
            while j < len(row):
                n = row[j]
                shape[i][j] = board[i][j] = 1
                print(i, j)
                # 앞쪽 검사
                jf = j -1
                while jf >= 0:
                    if board[i][jf] == 0:
                        shape[i][jf] = board[i][jf] = 1
                        print(i, jf, "jf")
                    jf -= 1
                j += 1
    return shape


def find_start(board):
    for i, row in enumerate(board):
        for j, n in enumerate(row):
            if n == 0:
                return i, j


if __name__ == "__main__":
    print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
                   [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]), 14)
    # print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]), 0)
