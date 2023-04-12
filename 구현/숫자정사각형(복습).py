import sys

N, M = map(int, sys.stdin.readline().split())  # 직사각형 행, 열 입력
rectangle = []

# 직사각형 생성
for _ in range(N):
    nums = list(map(int, sys.stdin.readline().strip()))   # 한글자씩 저장
    rectangle.append(nums)
#print(rectangle)

square = []   # 만들 정사각형
ans = 1
# 정사각형 만들기
for i in range(N):
    for j in range(M):
        for k in range(ans, min(N, M)):   # 현재 본것의 뒷부분 확인
            if N <= i + k or M <= j + k:  # 범위를 벗어난 경우 중단
                break
            if rectangle[i][j] == rectangle[i+k][j] == rectangle[i][j+k] == rectangle[i+k][j+k]:
                ans = max(ans, k + 1)  # 정사각형의 길이

print(ans**2)




