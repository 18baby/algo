# 함수 없이 풀기
str = input()

count = 0
for i in range(len(str)-1):
    if str[i] != str[i+1]:
        count += 1
        #print(i, i+1)

answer = (count // 2) + (count % 2)
print(answer)


# 문자열 분리 함수 이용
s_set = set(str)
if ('1' in s_set) and ('0' in s_set):
    str1 = str.split('1')
    print(str1)
    count = 0
    for s in str1:
        if s == '':
            count += 1
    answer = (count // 2) + (count % 2)
    print(answer)

else:
    print(0)