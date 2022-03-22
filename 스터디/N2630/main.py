from sys import stdin

n = int(stdin.readline())
board = []
w_count = 0
b_count = 0

for i in range(n):
    board.append(list(map(int, stdin.readline().split())))

print(board)
