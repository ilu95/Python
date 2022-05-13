from sys import stdin

t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    if 1 <= n <= 100000:
        array = []
        array = [[0]*n for _ in range(2)]
        for i in range(2):
            array[i] = list(map(int, stdin.readline().split()))

        # n이 1인 경우
        if n == 1:
            print(max(map(max, array)))
            continue

        array[0][1] += array[1][0]
        array[1][1] += array[0][0]

        # 각 칸에 대한 경우의 수에서의 최댓값 저장
        for i in range(2, n):
            array[0][i] += max(array[1][i-2], array[1][i-1])
            array[1][i] += max(array[0][i-2], array[0][i-1])

        # 모든 경우의 수에서의 최댓값 출력
        print(max(map(max, array)))
