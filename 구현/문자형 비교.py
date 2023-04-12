s_num = input()    # 문자로 입력
c_num = s_num
count = 0

# 두자리수 문자로 만들기
if int(s_num)<10:
    s_num = '0'+s_num

while True:
    first = (int(c_num[0]) + int(c_num[1]))%10
    new_num = c_num[0] + str(first)
    if s_num == new_num:
        break
    else:
        count += 1

print(count)