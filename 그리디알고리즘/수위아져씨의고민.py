import sys


# 최소거리 함수 <- 수정 필요
def manhattan_d(A, B):
    d = 0
    for i in range(2):    # 2차원 공간
        d += abs(A[i]-B[i])
    return d


T = int(input())   # 테스트 케이스 입력

for _ in range(T):
    F, R, N = map(int, sys.stdin.readline().split())    # F: 빌딩 높이, R:한 층당 사무실수, N:불켜진 사무실수
    switch_on = []   # 불이 켜진 좌표들 저장

    for _ in range(N):
        obj = list(map(int, sys.stdin.readline().split()))  # 불 켜진 집 좌표
        switch_on.append(obj)  # 불켜진집 추가
    #print(switch_on)  
    switch_on.sort(key=lambda x:x[0])    # 층 순서대로 정렬
    
    up_list = []      # 올라갈때 들릴 호실들
    down_list = []    # 내려올때 들릴 호실들
    # 중간호실 기준 방문 호실들 정리
    for i in range(len(switch_on)):
        if switch_on[i][0] <= (R // 2) + 1:
            up_list.append(switch_on[i])
        else:
            down_list.append(switch_on[i])
    
    total_d = 0   # 최소가 되는 이동거리
    for i in range(len(up_list)):
        total_d += F                    # 층이동
        total_d += (up_list[i][1] * 2)  # 호실 이동
    for i in range(len(down_list)):
        total_d += F                    # 층이동
        total_d += ((R - up_list[i][1]+1) * 2)  # 호실 이동
    
    print(total_d)

# 전광판을 끄기 전에는 왼쪽에 있는 엘리베이터만 탈 수 있고, 끈 이후에는 오른쪽에 있는 엘리베이터만 탈 수 있다  <- 이게 뭔 뜻?
