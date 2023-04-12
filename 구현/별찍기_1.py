N = int(input())
for i in range(1, N+1):
    for j in range(i):
        print('*', end='')  # 출력 개행문자 제거
    if i != N:
        print("")