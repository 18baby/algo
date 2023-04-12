import sys


def change_data(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


n = int(sys.stdin.readline())  # 기타 개수

guitar = []   # 시리얼 번호 저장
len_data = []
for i in range(n):
    item = input()
    len_data.append([i, len(item)])
    guitar.append(item)

print(guitar)
print(len_data)
s_guitar = guitar.copy()

# 조건1 데이터 길이순으로 정렬
len_data.sort(key=lambda x: (x[1]))
for i in range(n):
    s_guitar[i] = guitar[len_data[i][0]]
print(s_guitar)

# 전체 배열을 탐색
for i in range(n-1):
    for j in range(i+1, n):
        # 조건 2 길이가 같으면 모든 자리수 합으로 결정
        if len(s_guitar[i]) == len(s_guitar[j]):
            #print(f'{i}같은 길이{j}')
            i_sum = 0   # 앞 인덱스의 합
            j_sum = 0   # 뒤 인덱스의 합
            # 문자 하나씩 숫자형이 있으면 합을 계산
            for i_cha in s_guitar[i]:
                if i_cha.isdigit():
                    i_sum += int(i_cha)
            for j_cha in s_guitar[j]:
                if j_cha.isdigit():
                    j_sum += int(j_cha)
            #print(i_sum, j_sum)
            if i_sum > j_sum:   # 총 합이 더 작은걸 앞으로 오게함
                change_data(s_guitar, i, j)
            
            # 조건3 알파벳 순 정렬
            elif i_sum == j_sum:
                for i_cha, j_cha in zip(s_guitar[i], s_guitar[j]):  # 두개의 반복문을 한번에 돌리는 코드
                    if i_cha > j_cha:
                        change_data(s_guitar, i, j)
                        break
                    elif i_cha < j_cha:
                        break

for i in s_guitar:
    print(i)
