from sys import stdin

n, m = map(int, stdin.readline().split())

map = []
res = 0
max = 0

for i in range(n):
    map.append(list(stdin.readline()))


def check(x, y):
    global res
    for i in range(min(n, m)):
        # print("------------------------\n\n")
        if x+i > n-1 or y+i > m-1:
            # print("범위 초과 현재 위치", x+i, y+i)
            return
        else:
            # print("x :", x, " / y : ", y, " / 길이 : ", i)
            # 네 꼭짓점의 숫자가 같은 경우
            if map[x][y] == map[x][y+i] and map[x][y+i] == map[x+i][y] and map[x+i][y] == map[x+i][y+i]:
                # print("탐색 범위 : ", map[x][y], map[x+i][y],
                #       map[x][y+i], map[x+i][y+i])
                test = (i+1)*(i+1)
                if test > res:
                    res = test
                    # print("최대 정사각형 넓이 :", res)


for x in range(n):
    for y in range(m):
        if y > min(n, m) or x > min(n, m):
            break
        check(x, y)

print(res)
