from itertools import count
from sys import stdin
import copy
from tracemalloc import start

n = int(stdin.readline())

board = []

# 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
res = []

for i in range(n):
    board.append(list(stdin.readline().strip()))


def check(x, y, copy_board, color):
    count_x = 1
    count_y = 1
    # print("\n\n현재 위치 :", x, y, "색깔 :", color)
    # print(copy_board)
    # 세로 확인
    for i in range(1, n):
        if x+i < n:
            if copy_board[x+i][y] != color:
                break
            if copy_board[x+i][y] == color:
                # print("아래로 확장", copy_board[x+i][y])
                count_x += 1
        if x-i >= 0:
            if copy_board[x-i][y] != color:
                break
            if copy_board[x-i][y] == color:
                # print("위로 확장", copy_board[x-i][y])
                count_x += 1
    # 가로 확인
    for i in range(1, n):
        if y+i < n:
            if copy_board[x][y+i] != color:
                break
            if copy_board[x][y+i] == color:
                # print("오른쪽으로 확장", copy_board[x][y+i])
                count_y += 1
        if y-i >= 0:
            if copy_board[x][y-i] != color:
                break
            if copy_board[x][y-i] == color:
                # print("왼쪽으로 확장", copy_board[x][y-i])
                count_y += 1
    res.append(max(count_x, count_y))

# 사탕의 색이 다른 인접한 두 칸 탐색 후 교환


def change(x, y):
    check(x, y, board, board[x][y])
    copy_board_x = copy.deepcopy(board)
    copy_board_y = copy.deepcopy(board)
    ny = y + 1
    nx = x + 1
    # 가로 탐색
    # 행동 1) 다른 색인 경우 고른 칸에 들어있는 사탕 서로 교환
    if ny < n:
        if board[x][y] != board[x][ny]:
            copy_board_y[x][y] = board[x][ny]
            copy_board_y[x][ny] = board[x][y]
            # 행동 2) 교환 후 최장 연속 부분 탐색
            check(x, y, copy_board_y, copy_board_y[x][y])
            check(x, ny, copy_board_y, copy_board_y[x][ny])
    # 세로 탐색
    if nx < n:
        # 행동 1) 다른 색인 경우 고른 칸에 들어있는 사탕 서로 교환
        if board[x][y] != board[nx][y] and nx < n:
            copy_board_x[nx][y] = board[x][y]
            copy_board_x[x][y] = board[nx][y]
            # 행동 2) 교환 후 최장 연속 부분 탐색
            check(x, y, copy_board_x, copy_board_x[x][y])
            check(nx, y, copy_board_x, copy_board_x[nx][y])


# 사탕의 색이 다른 인접한 두 칸 탐색
for x in range(n):
    # print("x줄 출력", board[x])
    for y in range(n):
        change(x, y)

# print(res)
print(max(res))
