# 입력
N, M = map(int, input().split())
price_list = []
cost = 0

# 가격표 입력
for i in range(M):
    price_set = list(map(int, input().split()))
    price_list.append(price_set)

price_list.sort(key=lambda x:x[0])   # 세트 가격에 대해서 정렬
min_set = price_list[0][0]
price_list.sort(key=lambda x:x[1])   # 낱개 가격에 대해서 정렬
min_item = price_list[0][1]

# N이 6의 배수일때 -> 최저가 6개 set 구매
if (min_item*6) > min_set:    # 낱개 6개 구입이 세트보다 더 싼 경우
    cost = (N//6) * min_set
else:                         # 세트 구입이 낱개 6개보다 더 싼 경우
    cost = (N//6) * (min_item*6)
    
# 낱개 계산이 필요할때
if N % 6 != 0:
    if (min_item*(N%6)) > min_set:  # 한 세트를 더 사는게 더 비쌀때낱개로 개수 맞춰서 사는게 더 쌀때
        cost += min_set
    else:                           # 낱개로 개수 맞춰서 사는게 더 쌀때
        cost += (N%6) * min_item

print(cost)
