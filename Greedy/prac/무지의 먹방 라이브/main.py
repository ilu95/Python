def solution(food_times, k):
    print(K, end="초 에서 네트워크 장애가 발생했습니다. ")
    answer = i
    return answer


try:
    # 먹어야 할 N개의 음식
    print("먹어야하는 음식의 수 : ")
    n = int(input())
    print("1번부터 n번까지의 음식을 먹을때 각각 필요한 시간 : ")
    Food_times = list(map(int, input().split()))
    print("네트워크 장애로 인한 딜레이 : ")
    K = int(input())

    time = 0
    i = 0

    while True:
        if time == K:
            break
        for i in range(n):
            print(time, "~", time+1, end="초 동안 ")
            if Food_times[i] == 0:
                print("(", i+1, end=" 번 음식은 다 먹었으므로) ")
                i += 1
            if Food_times[i] != 0:
                Food_times[i] -= 1
            print(i+1, end="번 음식을 섭취한다. 남은 시간은 [")
            for j in range(n):
                print(Food_times[j], end=", ")
            print("] 입니다.")
            time += 1
            # K초에 네트워크 발생하면 solution 실행
            if time == K:
                i -= 1
                answer = solution(Food_times, K)
                print(answer, "번 음식을 섭취해야 할 때 중단되었으므로, 장애 복구 후에",
                      answer, "번 음식부터 다시 먹기 시작하면 됩니다.")
                break
except EOFError:
    exit
