import sys
from heapq import heappush, heappop

# N: 도시개수, M: 도로개수, K: 거리정보, X: 시작점 번호
N, M, K, X = map(int, sys.stdin.readline().split())

# 드래프 생성
graph = [[] for i in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))   # 연결된 노드, 가중치
#print(graph)

# 최소거리 저장 리스트
Inf = 1e+7
distance = [Inf] * (N+1)


# 다익스트라 알고리즘
def dijkstra(start):
    heap = []
    distance[start] = 0
    heappush(heap, (0, start))   # heap에 시작 노드 추가

    # heap이 빌때까지 반복
    while heap:
        # 최단 길이 가져오기
        dist, node = heappop(heap)
        # 현재 노드가 이미 최단거리라면 무시
        if distance[node] < dist:
            continue
        # 인접한 다른 노드들 확인
        for i in graph[node]:
            cost = dist + i[1]
            # 최단 경로 확인
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))

# 알고리즘 실행
dijkstra(X)
#print(distance)

k_list = []    # 최단 거리가 k인 노드들 저장
for i in range(1, N+1):
    if distance[i] == K:
        k_list.append(i)
k_list.sort()
#print(k_list)
if len(k_list) == 0:
    print(-1)
else:
    for i in k_list:
        print(i)








