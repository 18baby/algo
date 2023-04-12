import sys

# 입력
n = int(sys.stdin.readline().rstrip())
A = set(map(int, sys.stdin.readline().split()))    # 파이선에서는 set이 hash 함수로 이루워져 탐색하는데 걸리는 시간이 O(1)이다!!
m = int(sys.stdin.readline().rstrip())
search = list(map(int, sys.stdin.readline().split()))

print(A)   # set은 자동 정렬
for i in range(m):
    if search[i] in A:
        print(1)
    else:
        print(0)

