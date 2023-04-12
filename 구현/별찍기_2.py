N = int(input())
for i in range(N):
    for j in range(N):
        if j >= N - (i+1):
            print('*', end='')  # 출력 개행문자 제거
        else:
            print(' ', end='')
    if i != N:
        print("")