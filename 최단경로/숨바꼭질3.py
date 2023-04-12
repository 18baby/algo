import sys
import heapq
input = sys.stdin.readline
max_len = int(1e+5)   # 그래프 최대 길이
Inf = 1e+9

N, K = map(int, input().split())   # n: 수빈위치, k: 동생위치

graph = [[] for i in range(max_len+1)]    # 그래프 생성 -> [이동 노드, 시간 저장]
graph[0].append([1, 1])
for i in range(1, max_len+1):
    graph[i].append([i+1, 1])
    graph[i].append([i-1, 1])
    graph[i].append([i*2, 0])

distance = [Inf] * (max_len+1)
def shortest(start, end):      # 다익스트라
    if start >= end:     # 시작점이 더 크면 뒤로가는 방법밖에 없음
        print(start - end)
        return 0
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for n in graph[node]:
            #print(n[0])
            if (0 <= n[0]) and (n[0] <= max_len):
                cost = n[1] + dist
                if cost < distance[n[0]]:
                    distance[n[0]] = cost
                    heapq.heappush(q, (distance[n[0]], n[0]))


m = shortest(N, K)
if m != 0:
    print(distance[K])

