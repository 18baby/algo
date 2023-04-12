size = int(input())   # 우리의 크기

dp = [0]*(size+1)     # 행별로 사자 마리수 저장
#print(dp)

# 초기화
for i in range(size + 1):   # [없음, 왼쪽, 오른쪽]
    dp[i] = [0, 0, 0]

# 첫번째 행 값 입력
for i in range(3):
    dp[1][i] = 1    # [현재 행번호][0 or 1 or 2]

# 두번째 행부터 계산 시작
for i in range(2, size + 1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

# 출력
print(sum(dp[size]) % 9901)