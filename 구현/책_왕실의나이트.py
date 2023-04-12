location = input()

row = location[0]   # 행 위치 -> 아스키 값 (a=97 , h=105)
col = location[1]   # 열 위치

def move(r, c):
    rows = [i for i in range(97, 106)]
    cols = [i for i in range(1, 9)]
    count = 0
    n_r = ord(r)

    steps = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, -2], [1, 2], [-1, 2], [-1, -2]]
    loc = [n_r, c]

    for i in range(8):
        moved = steps[i] + loc
        if (moved[0] >= 97) and (moved[0] <= 105):
            if (moved[0] >= 1) and (moved[0] <= 9):
                count += 1

    return count

answer = move(row, col)
print(answer)

