# 데이터 입력
n = int(input())  # 국회의원 수
votes = []

for i in range(n):
    gain = int(input())
    votes.append(gain)

dasom = votes[0]           # 다솜이 투표수
votes.sort(reverse=True)   # 투표수 정렬
count = 0                  # 매수 인원수

# 무한루프 방지
if len(votes) == 1:
    print(0)
    
while votes[0] >= dasom:
    dasom += 1
    votes[0] -= 1
    count += 1
    votes.sort(reverse=True)
print(count)
