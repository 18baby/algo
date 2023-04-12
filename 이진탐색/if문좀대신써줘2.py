import sys
from bisect import bisect_left   # 이진 탐색을 빠르게 할 수 있는 라이브러리

input = sys.stdin.readline

n, m = map(int, input().split())
title = []
power = []

for _ in range(n):
    a, b = input().split()
    title.append(a)
    power.append(int(b))

for _ in range(m):
    print(title[bisect_left(power, int(input()))])
    # bisect_left(arr, b) : b가 arr에 (정렬을 유지하면서)들어갈 수 있는 가장 왼쪽 인덱스 반환
