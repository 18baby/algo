import sys
import heapq
INF = 1e+9
input = sys.stdin.readline

N = int(input())   # 도시 개수
M = int(input())   # 버스 개수

graph = [[] for i in range(N+1)]  # 도시 연결 상태
for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

# 탄색할 시작점, 끝점
m_s, m_e = map(int, input().split())

distance = [INF]*(N+1)
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))

    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for n in graph[node]:
            cost = n[1] + dist   # 꺼낸 노드까지 가중치 계산
            if cost < distance[n[0]]:
                distance[n[0]] = cost
                heapq.heappush(q, (distance[n[0]], n[0]))

# 알고리즘 학습
dijkstra(m_s)
print(distance[m_e])
            