import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())  # 노드개수, 간선개수

graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, a, b])    # [가중치, 간선] 순으로 저장 -> 우선순위 큐를 위해
    graph[b].append([cost, b, a])
#print(graph)

visited = [0]*(v+1)   # 노드 방문 여부 확인


# 프림 알고리즘
def prim(graph, start):
    visited[start] = 1  # 방문 표시
    q = graph[start]    # 시작노드와 연결된 노드들 저장
    heapq.heapify(q)    # 우선순위 큐 생성 -> 연결된 노드들을 가중치 낮은 순으로 정렬
    mst = []     # mst 구성 간선들 저장
    result = 0   # 최소 간선 합
    while q:
        cost, a, b = heapq.heappop(q)   # 가중치 가장 작은 간선 선택
        if visited[b] == 0:   # 아직 미방문 노드 -> 싸이클 형성 방지
            visited[b] = 1
            mst.append((a, b))  # 간선 추가
            result += cost
            # 새로 넣은 노드와 인접한 간선들 탐색
            for edge in graph[b]:
                if visited[edge[2]] == 0:      # 싸이클 방지
                    heapq.heappush(q, edge)    # 싸이클이 없으면 해당 간선도 추가
    return result


print(prim(graph, 1))
