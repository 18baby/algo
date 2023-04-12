import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())   # N: 학생수, M: 키 비교 횟수
indegree = [0] * (N+1)    # 진입 차수
graph = [[] for _ in range(N+1)]

# 그래프 입력
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
# 키순으로 저장된 그래프이므로 DAG 조건(싸이클 없는 방향그래프)을 만족!!


# 위상정렬 실행
def topology_sort():
    q = deque()   # 노드 정렬 순으로 대입
    result = []   # 위상정렬 결과
    # 초기 시작 지점들 확인
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()   # 덱에서 노드 하나씩 꺼냄
        result.append(now)  # 꺼낸 순으로 위상정렬
        # 연결된 노드들 확인
        for node in graph[now]:
            indegree[node] -= 1   # 뺀 노드와 연결된 간선 제거
            if indegree[node] == 0:
                q.append(node)

    return result


answer = topology_sort()
for i in answer:
    print(i, end=' ')

