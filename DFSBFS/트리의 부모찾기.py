import sys
sys.setrecursionlimit(1000000)


def dfs(g, num, parent):
    for node in g[num]:
        if parent[node] == 0:    # 아직 연결이 안된 노드
            parent[node] = num   # 다음 노드에 부모 노드 저장
            dfs(g, node, parent)


n = int(sys.stdin.readline())  # 노드 개수

# 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())  # 간선 정보 입력
    graph[a].append(b)
    graph[b].append(a)

#print(graph)
parents = [0]*(n+1)       # 현재 자신의 위치에서 부모 노드의 정보 저장
dfs(graph, 1, parents)    # 1번 노드를 루트로 하는 트리 탐색 (1번부터 탐색하면 1번이 루트가 된다!!

#print(parents)
# 출력
for i in range(2, n+1):
    print(parents[i])
