import sys
import heapq

input = sys.stdin.readline


# 위상정렬
def topology_sort():
    q = []          # 낮은 번호부터 출력하기 위해 우선순위 큐 사용
    result = []
    for k in range(1, n+1):    # 번호 낮은 문제들 부터 추출
        if indegree[k] == 0:
            heapq.heappush(q, k)

    while q:
        now = heapq.heappop(q)   # 번호 낮은 것 부터 추출
        result.append(now)    # 가장 번호가 낮은애를 대입
        # 연결된 노드들 확인
        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                heapq.heappush(q, node)
    return result


t = int(input())  # 테스트 케이스 수
for i in range(t):
    n = int(input())  # i번째 테스트의 팀의 개수
    ly_rank = list(map(int, input().split()))    # 작년 순위
    print(f"작년 순위: {ly_rank}")
    m = int(input())  # 순위가 변한 팀 개수
    graph = [[] for _ in range(n+1)]  # 그래프 생성
    indegree = [1]*(n+1)      # 진입 차수 설정
    indegree[ly_rank[0]] = 0  # 작년 1등의 진입차수 제거
    print(f"기존 집입차수{indegree}")
    print("올해 순위 변동")
    for j in range(m):
        a, b = map(int, input().split())
        print(f"(작년기준){a}팀 순위: {ly_rank.index(a)}, {b}팀 순위: {ly_rank.index(b)}")
        # 변화된 등수 비교 -> 순위 반영
        if ly_rank.index(a) > ly_rank.index(b):
            graph[a].append(b)
        else:
            graph[b].append(a)
    print(graph)
    ty_rank = topology_sort()
    print(f"위상 정렬 결과: {ty_rank}")
    print()
