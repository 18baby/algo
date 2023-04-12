n = int(input())    # 로프 개수
max_w_list = []
max_w = 0

for i in range(n):
    w = int(input())      # 각 로프별 들 수 있는 최대 중랼
    max_w_list.append(w)  # 로프 별 들 수 있는 최대값 저장

max_w_list.sort(reverse=True)  # 큰 값부터 정렬
#print(max_w_list)

max_list = []
for i in range(1, n+1):
    max_list.append(max_w_list[i-1]*i)  # 로프별 들 수 있는 개수

print(max(max_list))

