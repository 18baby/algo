import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

count = 0
arr.sort()
#print(arr)

i = 0
j = len(arr) - 1
while i < j:
    hap = arr[i] + arr[j]
    if hap == x:
        count += 1
        i += 1
    elif hap < x:
        i += 1
    else:
        j -= 1
print(count)


# 시간 초과
# count=0
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]+arr[j] == x:
#             count += 1
# print(count)