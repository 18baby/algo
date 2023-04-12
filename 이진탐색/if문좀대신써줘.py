import sys

N, M = map(int, sys.stdin.readline().split())   # N: 칭호 개수, M: 캐릭터 개수

names = []    # 칭호 저장
powers = [-1]   # 상한값 저장
for _ in range(N):
    name, power = sys.stdin.readline().split()
    power = int(power)
    if power != powers[-1]:   # 중복되는 상한 값은 하나의 이름으로만 설정
        names.append(name)
        powers.append(power)  # power는 정렬된 상태로 주어짐
powers.pop(0)  # 첫번째 비값 제거
#print(names)
#print(powers)  # power들을 오름차순으로 주어짐

for i in range(M):
    low = 0
    high = len(names) - 1
    power = int(sys.stdin.readline().strip())
    #print(f'입력값: {power}')
    while low <= high:
        mid = (low + high) // 2
        #print(low, mid, high)
        if power < powers[mid]:
            high = mid - 1
        elif power > powers[mid]:
            low = mid + 1
            mid = low   # 종료시 받을 값
        else:
            break
    print(names[mid])