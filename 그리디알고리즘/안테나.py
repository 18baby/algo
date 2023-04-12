N = int(input())     # 집의 개수
h_location = list(map(int, input().split()))    # 각 집들의 위치

h_location.sort()   # 집 위치 정렬
median = (N-1)//2   # 중간값 <- 거맃 최소가 되는 집의 위치(동일시 앞 인덱스)

#print(h_location)
print(h_location[median])
