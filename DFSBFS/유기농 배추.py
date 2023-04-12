import sys
sys.setrecursionlimit(10000)
input1 = sys.stdin.readline


def dfs(g, x, y):
    if (x <= -1) or (y <= -1) or (x >= m) or (y >= n):
        return False
    if g[x][y] == 0:    # 채울 수 있는 공간이면
        g[x][y] = 1     # 방문한 것으로 확인
        # 상,하,좌,우 모두 이동해본다.
        dfs(g, x+1, y)
        dfs(g, x-1, y)
        dfs(g, x, y+1)
        dfs(g, x, y-1)
        return True
    return False


t = int(input1())  # 테스트 케이스 수

for _ in range(t):
    m, n, k = map(int, input1().split())  # 가로(m), 세로(n), 배추개수(k)
    c_map = [[1 for c in range(n)] for r in range(m)]  # 배추 위치 표시(배추o -> 0, 배추x -> 1)
    # 그래프 생성
    for i in range(k):
        x_n, y_n = map(int, input1().split())
        c_map[x_n][y_n] = 0   # 배추 위치 표시

    count = 0  # 독립적인 그래프 개수 확인
    # 그래프 탐색 진행
    for i in range(n):
        for j in range(m):
            if dfs(c_map, i, j):
                count += 1
    print(count)
