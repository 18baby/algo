n = int(input())
moves = input().split()

point = [1, 1]
new_point = [1, 1]
move = ['L', 'R', 'U', 'D']

for s in moves:
    if s in move:
        if s == 'L':
            #print('L')
            new_point[1] = point[1] - 1
        elif s == 'R':
            #print('R')
            new_point[1] = point[1] + 1
        elif s == 'U':
            #print('U')
            new_point[0] = point[0] - 1
        elif s == 'D':
            #print('D')
            new_point[0] = point[0] + 1
    # 네모 박스 안에서 진행
    if (new_point[0] >= 1) and (new_point[1] >= 1):
        #print('success')
        point = new_point.copy()
    else:
        #print('fail')
        new_point = point.copy()
    #print(point)

print(point)




