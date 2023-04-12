N, L = map(int, input().split())       # N: 물이 새는 곳 위치, L: 가지고 있는 테이프 길이
arr = list(map(int, input().split()))  # 물 새는 위치 (1000이하)

arr.sort()  # 배열 오름차순 정렬
#print(arr)

count = 0       # 테이프 사용 개수
taped = [0, 0]  # 가장 가까운 테이프 붙은 위치

# for i in range(arr[len(arr)-1]+1):    <- 처음에 생각한 식 (비효율적)
for i in arr:
    #print(i)
    if (i >= taped[0]) and (i <= taped[1]):  # 이미 테이프가 붙여진 위치
        continue

    if i in arr:   # 테이프 붙이기
        taped[0] = i          # 테이프 붙인 시작 위치
        taped[1] = i + L - 1  # 테이프 붙인 끝 위치
        count += 1
        #print(taped)

print(count)




