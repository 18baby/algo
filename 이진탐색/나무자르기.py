import sys

N, M = map(int, sys.stdin.readline().split())   # N: 나무수, M: 필요 나무 길이
trees = list(map(int, sys.stdin.readline().split()))  # 1줄의 나무 길이

low, high = 1, max(trees)    
# 자를 나무의 높이를(H) 기준으로 이진 탐색 => [새로운 접근법!!!]
while low <= high:
    mid = (low + high) // 2  # 자를 나무의 중간값
    cuts = 0
    # 파이선 for문시 인덱스로 하면 시간이 더 오래걸림!!
    for tree in trees:
        if tree > mid:
            cuts += tree - mid
    # 잘린 값을 기준으로 이분 탐색
    if cuts >= M:
        low = mid + 1
    else:
        high = mid - 1
# 최종적으로 가장 큰 H값 출력
print(high)
