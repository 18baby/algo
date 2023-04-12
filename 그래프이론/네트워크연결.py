import sys
input = sys.stdin.readline


# 루트 노드 찾기
def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]


# union 연산
def union_parent(parent, a, b):
    a = find_root(parent, a)  # a의 소속 집합
    b = find_root(parent, b)  # b의 소속 집합
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())   # 컴퓨터 수(노드 수)
M = int(input())   # 연결선 개수(간선 수)

parent = [i for i in range(N+1)]   # 자기자신 부모 설정
edges = []    # 가중치들 저장
result = 0    # 최소 비용
#print(parent)

# 그래프 입력
for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
edges.sort()    # 가중치 순 정렬

for edge in edges:
    # 사이클 미형성 간선만 선택
    if find_root(parent, edge[1]) != find_root(parent, edge[2]):
        union_parent(parent, edge[1], edge[2])   # 서로소 집합 형성
        result += edge[0]

print(result)
    

