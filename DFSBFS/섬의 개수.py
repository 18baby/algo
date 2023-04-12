import sys
sys.setrecursionlimit(10000)
input1 = sys.stdin.readline

while True:
    w, h = map(int, input1().split())   # w:너비, h:높이
    # 종료 조건
    if w == 0 and h == 0:
        break
    
    # 지도 입력
    maps = []
    for i in range(h):
        line = list(map(int, input1().split()))  # 한줄 입력
        maps.append(line)    # 지도 생성

    graph = maps.copy()
    print(graph)
    count = 0
    
    def dfs(g, x, y):  # w=x , h=y
        if x <= -1 or x >= w or y <= -1 or y >= h:
            return False
        if g[x][y] == 1:   # 육지라면 탐색 시작
            g[x][y] = 0    # 현재 위치 체크
            # 상하좌우, 대각선 탐색
            dfs(g, x+1, y)
            dfs(g, x-1, y)
            dfs(g, x, y+1)
            dfs(g, x, y-1)
            dfs(g, x+1, y+1)
            dfs(g, x+1, y-1)
            dfs(g, x-1, y+1)
            dfs(g, x-1, y-1)
            return True
        return False

    for y_n in range(h):
        for x_n in range(w):
            if dfs(graph, x_n, y_n):
                count += 1

    print(count)