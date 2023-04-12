## 다시 풀어보기
k, s, n = input().split()
n = int(n)
moves = []
for i in range(n):
    m = input()
    moves.append(m)

steps = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

# 현재 위치 정보 저장
king = [ord(k[0]), int(k[1])]
stone = [ord(s[0]), int(s[1])]

#print(king)
#print(stone)

for i in range(n):
    m = moves[i]
    if m in steps:
        nkr = king[0] + steps[m][0]
        nkc = king[1] + steps[m][1]
        if (65 <= nkr <= 72) and (1 <= nkc <= 8):
            if (nkr == stone[0]) and (nkc == stone[1]):
                nsr = stone[0] + steps[m][0]
                nsc = stone[1] + steps[m][1]
                if (65 <= nsr <= 72) and (1 <= nsc <= 8):
                    king = [nkr, nkc]
                    stone = [nsr, nsc]
            else:
                king = [nkr, nkc]

print(f'{chr(king[0])}{king[1]}')
print(f'{chr(stone[0])}{stone[1]}')
    
        
       



