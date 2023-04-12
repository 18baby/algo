import sys
# 공통 조상을 찾을때 같은 뿌리 내에 있으면 촌수 계산이 틀려짐!!

# 트리 노드 객체
class Node:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, node):
        self.child.append(node)

    def add_parent(self, node):
        self.parent = node

    # 루트노드, 루트노드까지의 거리 찾기 함수
    def find_root_count(self):
        node = self  # 현재 탐색 노드 위치
        count = 0
        while node.parent is not None:
            p = node.parent  # 부모 노드
            node = p   # 현재 탐색 노드 이동
            count += 1
        return node, count


n = int(sys.stdin.readline())   # 전체 사람 수
a, b = map(int, sys.stdin.readline().split())   # 촌수를 계산할 두 사람
m = int(sys.stdin.readline())   # 부모-자식 관계 개수

# 트리 생성
tree = [0]*(n+1)
for i in range(1, n+1):
    tree[i] = Node(i) 

# 연결관계 설정
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())  # 부모, 자식
    tree[x].add_child(tree[y])
    tree[y].add_parent(tree[x])

a_root, a_count = tree[a].find_root_count()
b_root, b_count = tree[b].find_root_count()

#print(a_root.data, b_root.data)
# 공통조상이 아닌경우
if a_root != b_root:
    print(-1)
# 공통 조상이 있는 경우
else:
    print(a_count + b_count)
