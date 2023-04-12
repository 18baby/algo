# 두 노드간의 간성의 길이만 구해주면 ok
N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []

# 노드 연결 상태 저장
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# dfs
def dfs(node, num):
    num += 1
    visited[node] = True
    if node == B:
        result.append(num)    # 두 노드가 연결되어 있음을 확인용
    for i in graph[node]:
        if not visited[i]:
            dfs(i, num)


dfs(A, 0)
if len(result) == 0:    # 그래프가 연결 되지 않은 상태
    print(-1)
else:
    print(result[0]-1)
