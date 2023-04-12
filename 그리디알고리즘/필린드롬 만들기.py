h_name = input()    # 필린드롭으로 만들 한수의 이름
#print(h_name)
l = len(h_name)     # 문자열 길이

dic = {}    # 각 문자별 개수 저장 사전
for i in range(l):
    if h_name[i] not in dic:
        dic[h_name[i]] = 1
    else:
        dic[h_name[i]] += 1

# 알파벳 순서대로 정렬
o_dict = dict(sorted(dic.items()))
d_l = len(o_dict)   # 사전의 길이
#print(o_dict)

count = 0   # 홀수 문자 개수
result = [] # 팰린드롭 결과 (앞 절반)

for s in o_dict:    # 사전을 돌면서 필린드롭 확인하기
    if o_dict[s] % 2 == 1:  # 홀수개인 문자 확인
        count += 1
        c = s       # 홀수개 문자 저장
    for i in range(o_dict[s] // 2):  # 문자별 앞 절반 생성
        result.append(s)
    if count > 1:    # 홀수개인 문자가 1개 이상인 경우 -> 팰린드롭 x
        print("I'm Sorry Hansoo")
        break

if count <= 1:   # 필린드롭 생성
    result = result + result[::-1]
    if l % 2 == 1: # 전체 길이가 홀수라면
        result.insert(l//2, c)
    answer = ''.join(result)
    print(answer)




