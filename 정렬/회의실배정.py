import sys

N = int(sys.stdin.readline())
meetings = [[0, 0]]*N
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())   # 시작, 종료 시간
    meeting = [s, e]
    meetings[i] = meeting

meetings.sort(key=lambda x: (x[1], x[0]))   # 끝나는 시간 기준 정렬(같으면 시작시간 빠른순)
#print(meetings)

s = meetings[0][0]  # 회의 시작
e = meetings[0][1]  # 회의 종료
count = 1
i = 1
# 어떤 회의가 뽑혔는지 확인용
#selected = [0]*N
#selected[0] = 1
while i < N:
    s = meetings[i][0]
    if s >= e:    # 시작 시간이 끝 시간 보다 늦으면 회의 채택
        e = meetings[i][1]  # 종료 시간 리셋
        count += 1
        #selected[i] = 1
    i += 1

#print(selected)
print(count)

