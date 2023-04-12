string = input()

# 문자열 변환
string = string.replace('XXXX', 'AAAA')
string = string.replace('XX', 'BB')
count = 0

for i in range(len(string)):
    if string[i] == 'X':
        print(-1)
        break
    count += 1

if count == len(string):
    print(string)

# 문자열 . 기준으로 분리 -> .의 개수를 알 수 없어서 힘듬!!
# pol = string.split('.')
# print(pol)
# end_count = 0
# for i in range(len(pol)):
#     if len(pol[i]) % 4 == 0:
#         for j in range(len(pol[i])):
#             pol[i][j] = 'A'
#     elif len(pol[i]) % 2 == 0:
#         for j in range(len(pol[i])):
#             pol[i][j] = 'B'
#     else:
#         print(-1)
#         end_count = 1
#
# if end_count == 0:
#     for i in range(len(string)):
#         if string[i] == '.':




