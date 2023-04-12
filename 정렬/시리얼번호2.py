import sys

# 성호 코드
n = int(input())

# serial 입력받기
serial = []
for i in range(n):
    m = sys.stdin.readline().strip()
    serial.append(m)
print('serial: ',serial)

# 사전 순 정렬(문자 정렬) 먼저
serial.sort()

# value 길이 추가
serial_dict = {x : [len(x),0] for x in serial}
print(serial_dict)

# value 숫자 합 추가
for key, value in serial_dict.items():
    cnt = 0
    ex = list(key)
    for k in ex:
        m = int(ord(k))
        if m >= 49 and m <= 57:   # 숫자인 문자일때
            cnt += (m - 48)
        else:
            continue
    value[1] = cnt

print('serial_dict: ',serial_dict)

final_serial = sorted(serial_dict.items(), key = lambda x : x[1])
print(final_serial)

for i in final_serial:
    print(i[0])