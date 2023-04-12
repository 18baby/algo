import sys


# DP알고리즘 -> O(n^2)
# 이전까지의 모든 수를 확인해 dp 업데이트
N = int(sys.stdin.readline().strip())   # 수열 A의 길이
A = list(map(int, sys.stdin.readline().split()))  # 수열 A
dp = [1]*N  # 현재 인덱스에서의 최대 부분 수열의 길이를 저장
#print(A)
#print(dp)
for i in range(N):
    for j in range(i):
        # 부분 수열 길이 추가하기 -> 전체범위 탐색
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
print('DP')
print(dp)
print(max(dp))


# 이진탐색 알고리즘 -> O(nlog(n))
# 이진 탐색으로 이전까지의 최대값 가져옴  [but] 길이만 맞출 수있음!!
import bisect

dp = [A[0]]   # 가장 긴 부분수열을 저장
for i in range(N):
    # 현재 수가 가장 큰수일때 -> 최대 부분수열에 추가
    if A[i] > dp[-1]:
        dp.append(A[i])
    else:
        # 현재 값을 필요한 위치에 대입 (by 이진탐색)
        idx = bisect.bisect_left(dp, A[i])
        dp[idx] = A[i]
print('bisection')
print(dp)
print(len(dp))


# 실제 최대 부분수열을 찾아내는 방법 (by DP) -> O(n^2)
dp = [1]*N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
# 최대 부분 수열 길이
print('find seq')
max_dp = max(dp)
print(max_dp)

# 최대 부분수열을 가지는 인덱스
max_idx = dp.index(max_dp)
seq = []  # 최대 부분 수열 저장
while max_idx >= 0:
    if dp[max_idx] == max_dp:
        seq.append(A[max_idx])
        max_dp -= 1
    max_idx -= 1

seq.reverse()
print(seq)