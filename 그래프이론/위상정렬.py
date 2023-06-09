from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)     # 모든 노드에 대한 진입차수는 0으로 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)    # 정점 A에서 B로 이동 가능
    indegree[b] += 1      # 진입 차수를 1 증가


# 위상 정렬 함수
def topology_sort():
    result = []     # 알고리즘 수행 결과를 담을 리스트
    q = deque()     # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입  -> 위상 정렬 시작 노드들
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)   # 큐에서 꺼내진 순서대로 정렬이 완료됨
        for i in graph[now]:
            indegree[i] -= 1  # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()