import sys

T = int(sys.stdin.readline())  # 테스트 케이스 수

for _ in range(T):
    applications = []   # 지원자들
    N = int(sys.stdin.readline())   # 지원자 숫자

    # 지원자 성적 입력
    for _ in range(N):
        application = list(map(int, sys.stdin.readline().split()))  # 지원자 정보
        applications.append(application)

    applications.sort()         # 서류 기준 정렬
    check = applications[0][1]  # 합격자의 면접 등수
    count = 1                   # 합격자수
    for i in range(N):
        if applications[i][1] < check:   # 합격 조건
            count += 1
            check = applications[i][1]

    print(count)
