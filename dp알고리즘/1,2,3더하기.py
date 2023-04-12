import sys

T = int(sys.stdin.readline().strip())

dp = [1, 2, 4]   # 1, 2, 3을 만드는 방법 고정
for j in range(3, 10):
    dp.append(dp[j - 1] + dp[j - 2] + dp[j - 3])
#print(dp)
for i in range(T):
    n = int(sys.stdin.readline().strip())
    print(dp[n-1])
