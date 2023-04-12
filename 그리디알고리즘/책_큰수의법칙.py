# 공백 구분 한줄 입력
n, m, k = map(int, input().split())  # n: 주어지는 자연수 개수, m: 더하기 횟수, k:연속으로 쓸 수 있는 수

data = list(map(int, input().split()))  # 사용자가 입력하는 자연수 개수 (n개를 띄어쓰기 단위로 입력)
#print(data)

data.sort(reverse=True)  # 리스트를 큰 순서대로 정렬
sum = 0
count = 0

for i in range(m):   # m번 더하기
    if count < k:   # k번 이하로 더했으면
        sum += data[0]
        #print(f'i번째 합={sum}')
        count += 1
    else:            # k번 초과로 더한경우
        sum += data[1]
        #print(f'i번째 합={sum}')
        count = 0

print(sum)

# 교재 코드 (수열 응용)
# 어짜피 가장큰수와 그다음 큰수가 더해지는 과정이 반복되므로 수열을 이용한다!
first = data[0]
second = data[1]

repeat = ((first*k) + second) * (m // (k+1))  # 반복합 개수
rest = first * (m % (k+1))   # 나머지 남는 개수

result = repeat + rest
print(result)
