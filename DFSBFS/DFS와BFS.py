# DFS 방식
def DFS(g, node_num, visit):
    visit[node_num] = True      # 현재 노드 방문 완료
    for num in g[node_num]:     # 연결된 노드들을 확인
        if not visit[num]:
            #print(f'{num}방문')    # 방문 노드 출력
            #print('재귀호출')
            print(num, end=' ')
            DFS(g, num, visit)


def BFS(g, node_num, visit):
    q = [node_num]
    visit[node_num] = True
    while q:    # 큐가 빌때까지 반복
        out = q.pop(0)
        print(out, end=' ')
        for i in range(len(g[out])):
            if not visit[g[out][i]]:      # 방문한적 없는 노드를 추가
                q.append(g[out][i])
                visit[g[out][i]] = True


n, m, v = map(int, input().split())   # n: 정점 개수, m: 간선개수, v: 탐색을 시작할 정점 번호

# 그래프 생성
graph = [[] for i in range(n+1)]   # 정점이 n개인 그래프 생성
for i in range(m):
    edge = tuple(map(int, input().split()))
    # 양방향 간선 추가
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

print(graph)
# 낮은 노드 순으로 정렬
for i in range(1, n+1):
    graph[i].sort()   
#print(graph)

visited = [False for i in range(n+1)]    # 방문여부
vis = visited.copy()

# DFS
print(v, end=' ')
DFS(graph, v, vis)
print()

# BFS
BFS(graph, v, visited)
