import sys
input = sys.stdin.readline


# 나의 방법 -> 오답 (중복 방지 필요!!)
N = int(input())   # 사람수
graph = [[] for i in range(N+1)]
for i in range(N):
    f_list = list(input().strip())
    for j in range(len(f_list)):
        if f_list[j] == 'Y':
            graph[i+1].append(j+1)   # 연결된 노드 추가
print(graph)
f_count = [0]*(N+1)   # 2-친구 개수 확인용
for i in range(1, N+1):
    count = len(graph[i])  # 직접 친구 개수
    for node in graph[i]:
        print(f"{i}와 연결된 노드: {node}")
        for n in graph[node]:
            if (n not in graph[i]) and (n != i):
                count += 1

    f_count[i] = count

print(f_count)
print(max(f_count))

