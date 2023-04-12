# 행렬A의 3x3 원소 뒤집기
def reverse():
    for r in range(i, i+3):
        for c in range(j, j+3):
            A[r][c] = 1 - A[r][c]


N, M = map(int, input().split())   # A행렬 행, 열
# A 행렬 입력 받기
A = [list(map(int, input().strip())) for _ in range(N)]   # 한글자씩 받는 함수 strip()
# B 행렬 입력 받기
B = [list(map(int, input().strip())) for _ in range(N)]

count = 0
# 변환 연산을 할 수 없는 경우
if (N < 3 or M < 3) and (A != B):
    count = -1

# 뒤집기 연산을 수행 후 3x3 부분의 [0][0] 만 비교 해서 같은지 다른지 확인!!
else:
    # 전 범위를 돌면서 연산 실행
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                reverse()   # A행렬 3x3 값 뒤집기
                count += 1

    if A != B:
        count = -1

print(count)








