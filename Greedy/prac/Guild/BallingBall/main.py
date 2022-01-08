n, m = map(int, input().split())

weight = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i, n):
        if weight[i] != weight[j]:
            count += 1


print(count)

# 시간복잡도 n의 제곱이 되서 비효율적
