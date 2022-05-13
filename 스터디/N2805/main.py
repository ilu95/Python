from sys import stdin

n , m = map(int, stdin.readline().split())

data = []
data = list(map(int, stdin.readline().split()))
# 길이가 긴 순으로 정렬
data.sort(reverse=True)
start = 0
end = max(data)

while (start <= end):
    mid = (start+end)//2
    total = 0
    # print("중간값",mid)
    for i in data:
        # 나무 자르기
        if i > mid:
            # print("자른 길이", i-mid)
            total += (i-mid)
        else:
            # 긴 순으로 정렬했기 때문에 기준 값보다 작은 경우 넘어감
            # print("잘라",i, mid)
            break
    
    if total < m:
        # print("많이 남네", result)
        end = mid - 1
    else:
        # print("부족하네", result)
        result = mid
        # 목표에 도달하면 종료
        if total == m:
            break
        start = mid + 1

print(result)