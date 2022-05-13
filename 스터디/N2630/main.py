from sys import stdin

n = int(stdin.readline())
board = []
count_w = 0
count_b = 0

for i in range(n):
    board.append(list(map(int, stdin.readline().split())))

print(board)
