import sys
INF = int(1e+9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 그래프 입력 -> 기존 가중치 값
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 진행  -> [D_ab = min(D_ab, D_ak + D_kb)] : k를 거쳐가는 것과 그냥 가는것을 비교하여 더 작은 경로 선택
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 업데이트된 최단경로 그래프 생성
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INF", end=" ")
        print(graph[i][j], end=" ")
    print()
