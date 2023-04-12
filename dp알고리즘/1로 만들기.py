X = int(input())

count = [0 for i in range(X+1)]  # i번째에 최소 연산 횟수 저장
print(count)

for i in range(2, X+1):
    count[i] = count[i-1] + 1    # 3번째 경우

    if (i % 3) == 0:    # 1번째 경우
        count[i] = min(count[i], count[i//3]+1)

    if (i % 2) == 0:    # 2번째 경우
        count[i] = min(count[i], count[i//2]+1)

print(count[X])
print(count)

