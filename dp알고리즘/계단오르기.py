import sys

N = int(sys.stdin.readline().strip())   # 계단의 개수

stair = [0]
# 계단 생성
for i in range(N):
    num = int(sys.stdin.readline().strip())
    stair.append(num)

#print(stair)
if N <= 2:
    print(sum(stair))

else:
    dp = [[0, 0] for i in range(N+1)]   # 인덱스를 맞추기 위해 N+1개 선택 -> [현재까지 최대값, 연속1칸오른개수]
    # 초기값 설정
    dp[1] = [stair[1], 1]             # 처음 값
    dp[2] = [dp[1][0] + stair[2], 2]  # 두번째 값

    #print(dp)
    # 나의 dp 알고리즘 [오류 존제]
    for i in range(3, N+1):
        if dp[i-1][1] >= 2:   # 이미 연속된 2칸을 밟았으면 2칸 점프 (조건2) => 연속 3칸 조건을 잘못 적용
            dp[i] = [dp[i-2][0] + stair[i], 1]
        else:
            # 두칸 점프가 더 유리
            if (dp[i-1][0] + stair[i]) <= (dp[i-2][0] + stair[i]):
                dp[i] = [(dp[i - 2][0] + stair[i]), 1]
            # 한칸 점프가 더 유리
            else:
                dp[i] = [(dp[i - 1][0] + stair[i]), dp[i - 1][1] + 1]
        print(dp)

    print(dp[N][0])



dp = [0] * N
if N <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]            # 처음 값
    dp[1] = stair[0] + stair[1] # 두번째 값
    # dp 점화식 이용해서 최대값 구하기
    for i in range(2, N):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    print(dp[-1])