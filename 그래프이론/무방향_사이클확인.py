import sys
input = sys.stdin.readline


# 무방향 그래프의 사이클 확인!!

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


# 그래프 입력
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 자기 노드 기준 부모 노드

# 초기 부모노드 설정: 자기 자신
for i in range(1, v + 1):
    parent[i] = i
cycle = False  # 사이클 발생 여부

# union 연산 실행
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):   # 싸이클 형성 확인
        cycle = True
        break
    union_parent(parent, a, b)

# 각 원소의 집합 출력
if cycle:
    print("싸이클 형성")
else:
    print("싸이클 형성 x")

# 3 3
# 1 2
# 1 3
# 2 3