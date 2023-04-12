import sys
input = sys.stdin.readline
INF = int(1e+9)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
#print(graph)

# 연결 안된것들 확인
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = INF

# 플로이드 워셜
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 연결 안된것들 확인
for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            graph[i][j] = 0
        else:
            graph[i][j] = 1
        print(graph[i][j], end=" ")
    print()

# 2차원 배열 출력
for i in graph:
    print(*i)
