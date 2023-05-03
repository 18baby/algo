import sys
input = sys.stdin.readline

s = input().strip()

z_count = 0   # 0 제거 횟수
b_count = 0   # 이진법 변환 횟수

while s != '1':
    for i in range(len(s)):
        if s[i] == '0':
            z_count += 1
    s = s.replace('0', '')
    len_s = len(s)
    b_s = bin(len_s)
    print(f"이진 변환 {b_s}")
    s = b_s.replace('0b', '')
    b_count += 1
    print(s)

solution = [z_count, b_count]
print(solution)