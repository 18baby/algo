import sys
input = sys.stdin.readline

# 크루스칼 알고리즘 구현

# 부모 찾기 -> 경로 압축 기법 적용(부모를 바로 업데이트)
def find_parent(parent, x):
    # 루트노드가 아니면 나올때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소집합 합치기 -> 더 작은 노드가 부모가 되도록 설정
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0]*(v+1)    # 서로소 집합 확인

for i in range(1, v+1):
    parent[i] = i
edges = []            # 모든 간선 저장
result = 0            # 최소 비용

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 1. 간선 배열 정렬
edges.sort()

for edge in edges:
    print(edge)
    # 사이클을 형성하지 않을때만(서로소 집합의 루트 비교) 최소신장트리로 추가
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):  
        union_parent(parent, edge[1], edge[2])   # 서로소 집합 생성
        result += edge[0]

print(result)

# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25