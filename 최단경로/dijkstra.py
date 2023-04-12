# 다익스트라 알고리즘 구현 연습
import sys
import heapq     # 힙 라이브러리
INF = int(1e+9)  # 무한 가중치

n, m = map(int, sys.stdin.readline().split())  # n: 노드개수, m:간선개수
# 그래프 생성
graph = [[] for _ in range(n+1)]  
# 그래프 입력
for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])   # (연결 노드, 길이정보 추가)

distance = [INF] * (n+1)    # 노드별 최단 길이
visited = [False] * (n+1)   # 노드 방문 여부
start = int(sys.stdin.readline().strip())   # 시작노드 생성


# 미방문 노드중 가장 길이가 짧은 노드 선택 함수
def get_smallest_node():
    min_val = INF
    index = 0    # 리턴값
    # 선형 탐색
    for i in range(1, n+1):
        if (distance[i] < min_val) and (not visited[i]):
            min_val = distance[i]
            index = i
    return index
            

# O(n^2)방식의 다익스트라 알고리즘
def dijkstra_n2(start):
    distance[start] = 0  # 시작점 초기화
    visited[start] = True
    # 연결된 노드들을 확인하면서 distance 갱신
    for j in graph[start]:
        distance[j[0]] = j[1]   # 최단거리 갱신
    # 최단경로에 노드를 하나씩 추가
    for i in range(1, n+1):
        now = get_smallest_node()   # 최단경로에 추가할 노드 선택
        visited[now] = True
        # 추가한 노드 기준으로 최단경로 갱신
        for j in graph[now]:
            distance[j[0]] = min(distance[now] + j[1], distance[j[0]])   # (추가노드 거쳐서 오기 vs 기존 경로 유지)


# O(mlogn)방식의 다익스트라 알고리즘  => heap을 사용해 시간복잡도 (n -> logn)
def dijkstra_mlogn(start):
    q = []   # 힙
    distance[start] = 0  # 시작 가중치 설정
    heapq.heappush(q, (distance[start], start))    # 힙 push -> [현재노드의 최단길이, 현재노드]
    
    # q가 빌때까지 알고리즘 반복
    while q:
        dist, node = heapq.heappop(q)     # 선택된 노드(가중치가 가장작은 노드)의 가중치, 노드값
        if dist > distance[node]:   # 이미 확인한 노드 통과 (확인 결과 선택 안된 노드)
            continue
        # 이미 확인한 노드가 아닐땐 연결된 노드들의 가중치 갱신
        for i in graph[node]:
            cost = dist + i[1]   # 추가한 노드 거쳐서 오는 최단 길이
            if cost < distance[i[0]]:   # 최단 길이 배열 업데이트
                distance[i[0]] = cost
                heapq.heappush(q, (distance[i[0]], i[0]))
