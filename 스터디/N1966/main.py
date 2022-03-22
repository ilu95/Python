from sys import stdin

case = int(input())


def check(n, m):
    count = 0  # 문서를 인쇄한 횟수
    for size in range(n):
        for num in range(len(data)):
            # 맨 앞장의 문서가 최중요 문서가 아닌경우 맨뒤로 이동
            if data[0] < data[data.index(max(data))]:
                temp = data.pop(0)
                m -= 1
                data.append(temp)
            if m < 0:
                m = len(data)-1
            # 최중요 문서가 제일 앞에 있는 경우 인쇄
            if data.index(max(data)) == 0:
                count += 1
                # 목표 문서가 인쇄된 경우
                if m == 0 and max(data) == data[m]:
                    print(count)
                    return
                data.pop(0)
                m -= 1


for i in range(case):
    n, m = map(int, input().split())
    data = []  # 데이터
    data = list(map(int, stdin.readline().split()))
    # 최중요 문서 찾기 위한 전체 문서 탐색
    check(n, m)
