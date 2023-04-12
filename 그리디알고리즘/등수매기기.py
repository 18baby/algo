import sys
N = int(input())   # 인원수

expect_rank = [0]*N    # 예상 등수 저장
for i in range(N):
    expect_rank[i] = int(sys.stdin.readline().rstrip())   # 입력 빠르게 받기, (\n제거 -> restrip)

expect_rank.sort()     # 크기순 정렬
#print(expect_rank)

answer = 0    # 불만도 합
for i in range(N):
    answer += abs(expect_rank[i] - (i+1))

print(answer)





