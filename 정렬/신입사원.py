import sys

T = int(sys.stdin.readline())  # 테스트 케이스 수

for _ in range(T):
    applications = []   # 지원자들
    N = int(sys.stdin.readline())   # 지원자 숫자

    # 지원자 성적 입력
    for _ in range(N):
        application = list(map(int, sys.stdin.readline().split()))  # 지원자 정보
        applications.append(application)

    #print('성적입력 완료')
    applications.sort()     # 서류 기준 정렬
    check = [0]*N           # 탈락자 표시
    for i in range(N):      # 현재 나의 위치
        for j in range(i):  # 나 이전의 위치
            if check[j] == 1:  # 이미 탈락자라면 패스
                continue
            if applications[i][1] > applications[j][1]:
                check[i] = 1
    #print(check)
    print(N - sum(check))