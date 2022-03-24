from sys import stdin
import copy

n = int(stdin.readline())

board = []

# 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count_x = 0
count_y = 0
res = []

for i in range(n):
    board.append(list(stdin.readline().strip()))


def check(x, y, copy_board, color):
    print("현재 위치 :", x, y, "색깔 :", color)
    global count_x
    global count_y
    # 범위를 범어난 경우
    if x > n or x < 0 or y > n or y < 0:
        return
    # 세로 탐색
    if
    check(x+1, y, copy_board, color)
    check(x-1, y, copy_board, color)
    # 가로 탐색
    check(y+1, y, copy_board, color)
    check(y-1, y, copy_board, color)


# 사탕의 색이 다른 인접한 두 칸 탐색 후 교환
def change(x, y):
    # 2 방향(오른쪽, 아래쪽) 탐색
    for i in range(2):
        copy_board = copy.deepcopy(board)
        ny = y + dy[i]
        if ny >= n:
            return
        # 범위를 벗어나면 탈출
        # 행동 1) 다른 색인 경우 고른 칸에 들어있는 사탕 서로 교환
        if board[x][y] != board[x][ny]:
            copy_board[x][y] = board[x][ny]
            copy_board[x][ny] = board[x][y]
            # 색깔 저장
            candy = copy_board[x][y]
            # 행동 2) 교환 후 최장 연속 부분 탐색
            check(x, y, copy_board, candy)
        nx = x + dx[i]
        if nx >= n:
            return
        # 행동 1) 다른 색인 경우 고른 칸에 들어있는 사탕 서로 교환
        if board[x][y] != board[nx][y]:
            copy_board[nx][y] = board[x][y]
            copy_board[x][y] = board[nx][y]
            # 색깔 저장
            candy = copy_board[x][y]
            # 행동 2) 교환 후 최장 연속 부분 탐색
            check(x, y, copy_board, candy)


# 사탕의 색이 다른 인접한 두 칸 탐색
for x in range(n):
    # print("x줄 출력", board[x])
    for y in range(n):
        change(x, y)

print(res)
print(max(res))
