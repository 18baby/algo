N, M = map(int,input().split())   # 가로, 세로 입력

i = 1  # 말 가로위치
j = 1  # 말 세로위치
count = 1  # 방문칸수

# 이동 조건은 한번씩 사용 할 수 있는 경우
if N >= 3 and M >= 7:
    count = 5    # 1~4번 조건 이동후
    M_left = M - 7
    count += M_left

# 이동 조건을 모두 사용 불가인 경우
else:
    if N >= 3:
        count = min(4, M)
    elif N == 2:
        count = min(4, (M+1)//2)
print(count)



