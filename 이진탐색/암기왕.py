import sys
import time

#start = time.time()
T = int(sys.stdin.readline().strip())   # 테스트 케이스 수

for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 수첩1 정수 개수
    note1 = set(map(int, sys.stdin.readline().split()))     # 집합으로 받아서 자동 정렬 시킴
    M = int(sys.stdin.readline().strip())  # 수첩2 정수 개수
    note2 = list(map(int, sys.stdin.readline().split()))

    for n in note2:
        if n in note1:
            print(1)
        else:
            print(0)

    #print(note1)
    #print(note2)
    #note1.sort()
    # 수첩2 기준 이진 탐색
    # for i in range(M):
    #     low = 0
    #     high = N - 1
    #     count = 0
    #     while low <= high:
    #         mid = (low + high)//2
    #         if note2[i] > note1[mid]:
    #             low = mid + 1
    #         elif note2[i] < note1[mid]:
    #             high = mid - 1
    #         else:
    #             count += 1
    #             break
    #     print(count)

#end = time.time()