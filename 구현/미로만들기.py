n = int(input())
moves = list(input())

# 미로 만들기
miro = [['#' for col in range(101)] for row in range(101)]
loc = [50, 50]   # 현재 위치 저장 초기 위치(50, 50)

direction = 3       # 현재 내가 바라보고 있는 방향 설정 -> (1: 동, 2:서, 3:남, 4:북)
# 방향 전환 -> (현재방향: 다음방향)
left_change = {1: 4, 2: 3, 3: 1, 4: 2}   # 왼쪽으로 방향 변화
right_change = {1: 3, 2: 4, 3: 2, 4: 1}   # 오른쪽으로 방향 변화

# 이동했던 좌표들 저장
locations = []
miro[50][50] = '.'  # 시작점
locations.append(loc.copy())

for i in range(n):
    #print(f'현재방향: {direction}')
    # 방향 전환 명령어
    if moves[i] == 'L':
        direction = left_change[direction]  # 방향전환
    if moves[i] == 'R':
        direction = right_change[direction] # 방향전환
    #print(f'이동후 방향: {direction}')
    # 앞으로 이동 명령어
    if moves[i] == 'F':
        if direction == 1:   # 동
            loc[0] += 1
        elif direction == 2: # 서
            loc[0] -= 1
        elif direction == 3: # 남
            loc[1] += 1
        elif direction == 4: # 북
            loc[1] -= 1
        locations.append(loc.copy())
        miro[loc[1]][loc[0]] = '.'

nxs = [i[0] for i in locations]
nys = [i[1] for i in locations]
nxs.sort()
nys.sort()

# 좌표별 최대, 최소값 계산
xmin = nxs[0]
xmax = nxs[-1]
ymin = nys[0]
ymax = nys[-1]

# 미로 출력
for r in range(ymin, ymax + 1):
    for c in range(xmin, xmax + 1):
        print(miro[r][c], end='')
    print()

