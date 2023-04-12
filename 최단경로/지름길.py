import sys
input = sys.stdin.readline   # override
INF = 1e+9

N, D = map(int, input().split())   # N: 지름길 개수, D: 총 길이

shortcut = []   # 지름길들 저장
# 지름길이 맞은 것들만 고르기
for i in range(N):
    start, end, length = map(int, input().split())   # 시작점, 끝점, 지름길 길이
    # 지름길이 더 오래걸리는 경우 or 도착지 이탈하는 경우  -> 지름길 아님
    if (end - start < length) or (end > D):
        continue
    shortcut.append([start, end, length])   # 지름길 추가
    
shortcut.sort(key=lambda x:x[1])   # 도착지점 기준 정렬
print(shortcut)

dp = [i for i in range(D+1)]   # 고속도로

for root in shortcut:
    dp[root[1]] = min(dp[root[1]], dp[root[0]] + root[2])   # 최단거리 갱신
    # 뒷부분 업데이트
    for i in range(1, D-root[1]+1):
        dp[root[1] + i] = dp[root[1]] + i
    print(f'{root[1]}까지 최단경로 =  {dp[root[1]]}')

# 확인용
for i in range(D+1):
    print(dp[i], end=' ')
    if i % 10 == 0:
        print()

answer = dp[-1]
print(answer)
