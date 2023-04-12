import sys
input1 = sys.stdin.readline

n = int(input1())   # 땅의 개수
land = [0 for i in range(n)]  # 땅 초기화

for i in range(n):
    info = list(map(int, input1().split()))    # 10 1 2 3 1 2 3 1 2 3 1
    soldiers = info[0]   # 현재 땅의 주둔 군인수    ->  10
    units = info[1:]     # 현재 땅의 주둔 군대번호들 ->  [1 2 3 1 2 3 1 2 3 1]

    # 시간 초과 코드(내꺼)
    # unit_set = set(units)       # 주둔 군대 집합화 -> [1 2 3]
    # max_val = 0
    # max_key = 0
    # for unit in unit_set:
    #     unit_count = units.count(unit)
    #     if unit_count > max_val:
    #         max_val = unit_count
    #         max_key = unit

    # 사전 뢀용 -> 시간 절감에 도움!
    max_val = 0
    max_key = 0
    dic = dict()
    for j in range(len(units)):
        num = units[j]
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
        if dic[num] > max_val:
            max_val = dic[num]
            max_key = num

    if (soldiers // 2) < max_val:
        land[i] = max_key
    else:
        land[i] = 'SYJKGW'

for i in range(n):
    print(land[i])

