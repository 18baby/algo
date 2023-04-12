import sys

n, m = map(int, input().split())  # 행수, 열수
# 각 행의 데이터 입력

# 2차원 데이터 입력받기
arr = [0 for _ in range(m)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

#print(arr) 확인용

# 각 줄별로 최소값 추출
max_num = 0
for i in range(n):
    min_num = min(arr[i])
    if min_num > max_num:
        max_num = min_num
        
print(max_num)