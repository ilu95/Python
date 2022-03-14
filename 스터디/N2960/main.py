from sys import stdin

count = 0
index = 0


def check(n):
    global count
    p = data.index(min(data))
    while True:
        for i in range(n):
            if data[i] % data[p] == 0:
                if data[i] not in box:
                    # print("\n\n")
                    # print("data[i] : ", data[i], "data[min] :", data[p])
                    count += 1
                    box.append(data[i])
                    # print("삭제한 숫자 :", data[i])
                    # print("box의 내용물 :", box)
                    if count == k:
                        print(box[k-1])
                        return
            # 한바퀴 다 돌았지만 count가 k보다 작을때 p값 갱신
            if i == n-1:
                p_data = list(set(data).difference(box))
                p = data.index(min(p_data))
                # print("p값 갱신 :", p)
                break


# 입력받기
n, k = map(int, stdin.readline().split())

data = []
# 삭제한 숫자를 담는 리스트 생성
box = []

# 2부터 N까지를 포함한 리스트 생성
for i in range(2, n+1):
    data.append(i)

# 지우지 않은 수 중 가장 작은수 삭제 후 그 수의 배수 삭제
# 삭제한 횟수가 K보다 작을 경우 위 과정 반복

# print("2부터N까지의 정수 :", data)

check(len(data))
