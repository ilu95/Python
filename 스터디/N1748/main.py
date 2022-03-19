from sys import stdin

n = int(stdin.readline())

res = 0
trash = [0, 9, 99, 999, 9999, 99999, 999999, 9999999, 99999999]
digit = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
num = 1
minus = 0

for i in digit:
    if n < i:
        break
    if n >= i:
        minus += trash[num]
        num += 1

res = n*num
res -= minus

print(res)
