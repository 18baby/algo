n, m = map(int, input().split())

ice = []
for _ in range(n):
    line = list(map(int, input()))    # (체워진 부분: 1), (얼음이 들어가는 부분: 0)
    ice.append(line)
#print(ice)


# 해당 위치와 연결된 모든 노드들을 방문
def dfs(x, y):
    if (x<=-1) or (y<=-1) or (x>=n) or (y>=m):
        return False
    if ice[x][y] == 0:    # 채울 수 있는 공간이면
        ice[x][y] = 1     # 방문한 것 확인
        # 상,하,좌,우 모두 이동해본다.
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        # 현재위치에서 DFS 실행
        if dfs(i, j):
            result+=1

print(result)