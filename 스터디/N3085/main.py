from sys import stdin

n = int(stdin.readline())

board = []
res = 0

for i in range(n):
    board.append(list(stdin.readline().strip()))


# 연속된 같은색 사탕 찾기
def check(board):
    global res
    count = 0
    x = 0
    y = 0
    color = board[0][0]
    while True:
        # 가로 확인
        for i in range(n):
            if board[x][i] != color:
                color = board[x][i]
            elif board[x][i] == color:
                count += 1
                if res < count:
                    res = count
        count = 0

        x += 1
        # 세로 확인
        for i in range(n):
            if board[i][y] != color:
                color = board[i][y]
            elif board[i][y] == color:
                count += 1
                if res < count:
                    res = count
        count = 0
        y += 1
        if x == n or y == n:
            break


# 사탕의 색이 다른 인접한 두 칸 탐색
for x in range(n):
    for y in range(n):
        box = []
        # 오른쪽 사탕과 색깔이 다른 경우
        if y+1 < n:
            if board[x][y] != board[x][y+1]:
                # 자리 바꾸기
                board[x][y+1], board[x][y] = board[x][y], board[x][y+1]
                check(board)
                # 원상복귀
                board[x][y+1], board[x][y] = board[x][y], board[x][y+1]
        # 아래쪽 사탕과 색깔이 다른 경우
        if x+1 < n:
            if board[x][y] != board[x+1][y]:
                if x+1 > n:
                    continue
                # 자리 바꾸기
                board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
                check(board)
                # 원상복귀
                board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
print(res)
