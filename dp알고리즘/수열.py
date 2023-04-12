n = int(input())   # 연속되는 수
number = list(map(int, input().split()))  # 입력 받은 수열

counter = [0, 1, 1, 2]   # (이전수, 현재 수까지 카운터, 현재까지 최대 길이, 연속된 [큰값:3, 같은값:2 작은값:1]값 확인)

# 초기화
counter[0] = number[0]
if number[0] > number[1]:
    counter[3] = 1
elif number[0] < number[1]:
    counter[3] = 3

for i in range(1, len(number)):
    counter[0] = number[i-1]

    if number[i] > counter[0]:   # 이전 수보다 큰 경우
        check = 3
        if counter[3] >= 2:   # 연속된 큰값이면
            counter[1] += 1
            counter[3] = check
        else:                     # 연속된 큰값이 깨짐
            counter[1] = 1
            counter[3] = 1        # 연속된 작은값으로 변경
    elif number[i] < counter[0]:   # 이전 수보다 작은 경우:
        check = 1
        if counter[3] <= 2:   # 연속된 작은값이면
            counter[1] += 1
            counter[3] = check
        else:                     # 연속된 작은값이 깨짐
            counter[1] = 1
            counter[3] = 3
    else:                         # 값이 갘은 경우
        counter[1] += 1

    counter[2] = max(counter[1], counter[2])  # 현재까지 최대 길이 갱신

print(counter[2])


# 모범 답안
N = int(input())
li = list(map(int, input().split()))

dp1, dp2 = [1]*N, [1]*N

for i in range(1, N):
    if li[i] <= li[i-1]:
        dp1[i] = max(dp1[i], dp1[i-1]+1)
    if li[i] >= li[i-1]:
        dp2[i] = max(dp2[i], dp2[i-1]+1)
print(max(max(dp1), max(dp2)))


