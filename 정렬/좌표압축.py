N = int(input())
arr = list(map(int, input().split()))

s_arr = sorted(arr)   # 정렬된 배열
idx_arr = [-1] * N    # 기존 배열의 인덱스 정보 저장
#print(arr)

dic = {}
j = 0
for i in range(N):
    if s_arr[i] not in dic:   # 사전에 없는 값
        dic[s_arr[i]] = j
        j += 1

for i in range(N):
    idx_arr[i] = dic[arr[i]]

for i in range(N):
    print(idx_arr[i], end=' ')

print()
print(*idx_arr)   # 리스트 한칸씩 뛰어서 출력
