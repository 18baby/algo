def dfs(g, node, visited):
    visited[node] = True
    for i in range(len(g[node])):
        if not visited[g[node][i]]:
            next_n = g[node][i]
            dfs(g, next_n, visited)


n = int(input())  # 컴퓨터 수
m = int(input())  # 간선 수

# 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):  # 간선 정보 입력
    edge = tuple(map(int, input().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
#print(graph)

visited = [True] + [False]*n
count = 0

dfs(graph, 1, visited)  # 1번 노드 부터 탐색 시작
#print(visited)
for i in range(1, n+1):
    if visited[i]:
        count += 1
print(count-1)


# 그래프 개수를 세어주는 코드
# count = 0
# j = 1
# while False in visited:    # 모든 노드를 반복할때까지 계속 반복
#     dfs(graph, j, visited)
#     count += 1
#     j += 1
# print(count)