import sys
from string import ascii_uppercase
read = sys.stdin.readline

alph = {}
for i in ascii_uppercase:
    alph[i] = 0

N = int(read())
for _ in range(N):
    temp = read().replace('\n', '')
    for i in range(len(temp)):
        alph[temp[i]] += 10 ** (len(temp)-i-1)

values = sorted(alph.items(), key=lambda x: -x[1])
ans = 0
cnt = 9
for i in values:
    if i[1] == 0:
        break
    ans += i[1]*cnt
    cnt -= 1
print(ans)
