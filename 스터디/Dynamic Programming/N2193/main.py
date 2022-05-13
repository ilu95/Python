from re import L
from sys import stdin

n = int(stdin.readline())
array = [0]*1000000
array[1] = 1
array[2] = 1

for i in range(3, n+1):
    array[i] = array[i-1]+array[i-2]

print(array[n])
