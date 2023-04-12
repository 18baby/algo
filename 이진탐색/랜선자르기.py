import sys

K, N = map(int, sys.stdin.readline().split())   # k: 가진 랜선 개수, n: 필요한 랜선 개수
lans = []   # k개 랜선 길이 저장
for i in range(K):
    lans.append(int(sys.stdin.readline().strip()))
lans.sort()
print(lans)

# 가장 짧은 랜선을 기준으로 이진 탐색
low, high = 1, lans[-1]
while low <= high:
    mid = (low + high) // 2
    print(f'l={low}, m={mid}, h={high}')
    lan_count = 0   # 만들 수 있는 랜선 개수
    for lan in lans:
        lan_count += lan//mid
    print(lan_count)
    if lan_count < N:     # 랜선의 길이가 길때
        high = mid - 1
    elif lan_count >= N:  # 랜선의 길이가 짧을때   * 최대값 아이디어 =>[최대값을 찾기 위해 등호를 넣어준다!!]
        low = mid + 1

# 최대값을 찾아야 하니까 high를 뽑는다!
print(high)
