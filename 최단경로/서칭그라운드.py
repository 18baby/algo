import sys
import heapq
input = sys.stdin.readline
Inf = 1e+9

n, m, r = map(int, input().split())   # n: 지역 개수, m: 수색 범위, r: 길의 개수
item_list = list(map(int, input().split()))  # 인덱스별 아이템 개수
item_list.insert(0, 0)
# 그래프 생성
graph = [[] for i in range(n+1)]
for i in range(r):
    a, b, cost = map(int, input().split())   # 시작점, 종점, 거리
    graph[a].append([b, cost])
    graph[b].append([a, cost])
print(graph)
print(item_list)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (distance[i[0]], i[0]))
     

get_item_list = [0]*(n+1)   # 인덱스 위치부터 시작시 얻을 수 있는 최대 아이템 개수 저장
for i in range(1, n+1):
    distance = [Inf] * (n+1)
    i_sum = 0
    dijkstra(i)
    print(f"{i}번째 distance 베열 {distance}")
    for j in range(1, n+1):
        if distance[j] <= m:
            print(f"갈수 있는 노드: {j}")
            i_sum += item_list[j]   # 아이템 개수 저장
    print(f"{i}번째 최대 아이템 개수: {i_sum}")
    get_item_list[i] = i_sum

print(get_item_list)     # index별 아이템 최대값 저장 리스트
print(max(get_item_list))


