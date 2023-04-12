import sys

# 입력
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
search = list(map(int, sys.stdin.readline().split()))

A.sort()  # A배열 정렬
#print(A)

for i in range(m):
    count = 0
    low = 0
    high = len(A) - 1
    mid = (high + low) // 2
    #print(f'{i+1}번째 수 확인')
    # 이진 탐색
    while low <= high:
        #print(f'mid = {mid}, low = {low}, high = {high}')
        mid = (high + low) // 2
        if search[i] > A[mid]:
            low = mid + 1
        elif search[i] < A[mid]:
            high = mid - 1
        else:
            count += 1
            break
    print(count)


# 이진 탐색 함수 구현
def bisearch(arr, data):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if data > arr[mid]:
            low = mid + 1
        elif data < arr[mid]:
            high = mid - 1
        else:
            break
    return mid
