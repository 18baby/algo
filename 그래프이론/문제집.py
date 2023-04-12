import sys
from collections import deque
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 문제수, M: 선수과목 쌍 개수
graph = [[] for i in range(N+1)]
indegree = [0]*(N+1)    # 진입 차수
# 그래프 생성
for i in range(M):
    a, b = map(int, input().split())   # a번 이후 b번을 풀어야 함
    graph[a].append(b)
    indegree[b] += 1
#print(graph)

# 위상 정렬
def topology_sort():
    q = []          # 낮은 번호부터 출력하기 위해 우선순위 큐 사용
    result = []
    for i in range(1, N+1):    # 번호 낮은 문제들 부터 추출
        if indegree[i] == 0:
            heapq.heappush(q, i)
    print(f"초기 큐: {q}")

    while q:
        now = heapq.heappop(q)   # 번호 낮은 것 부터 추출
        print(f"pop 이후 큐: {q}")
        result.append(now)    # 가장 번호가 낮은애를 대입
        # 연결된 노드들 확인
        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                heapq.heappush(q, node)
                print(f"추가 후 큐: {q}")
    return result


# 위상 정렬된 순서
sorted_list = topology_sort()
for i in range(N):
    print(sorted_list[i], end=' ')
