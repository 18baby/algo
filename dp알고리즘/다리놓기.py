import sys

T = int(sys.stdin.readline().strip())   # 테스트 케이스 수
dp = [[0]*31 for _ in range(31)]        # dp 최대공간 생성

# dp 알고리즘 -> [N의 맨위를 이동 or 이동 x] => 인덱스 맞추기 위해 첫행 버림
for i in range(31):
    if i == 0:
        continue
    dp[i][i] = 1
    for j in range(i+1, 31):
        if i == 1:
            dp[i][j] = j
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]  # dp 알고리즘
#print(dp)

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())   # N: 서쪽, M: 동쪽  N<=M
    print(dp[N][M])

            


