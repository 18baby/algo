# 데이터 입력
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# s의 최솟값만 구하면 되므로 A, B둘다 정렬해서 곱해주면 되지만 그래도 B를 고정 후 A 리스트를 구하는 코드를 만들어 보자!
if (len(A) != n) or (len(B) != n):
    print('제대로 입력하세요')
else:
    # [문제 조건 무시 그리디]
    sorted_A = sorted(A)   # A 배열 정렬
    sorted_B = sorted(B, reverse=True)   # B 배열 내림차순 정렬
    s = 0
    for i in range(n):
        s += sorted_A[i] * sorted_B[i]

    # [내가 푼 방식 -> 정렬된 A까지 확인 가능]
    new_A = [0 for i in range(n)]  # s를 최소로 만드는 A 배열
    new_B = B.copy()
    sorted_index = []              # 내림 차순으로 정렬된 B 배열의 인덱스 값 저장
    s1 = 0
    # 정렬된 B 리스트의 인덱스값 저장
    for i in range(n):
        max_index = new_B.index(max(new_B))
        sorted_index.append(max_index)
        new_B[max_index] = -1
    # s를 최소로 만드는 A 배열 생성
    for i in range(n):
        new_A[sorted_index[i]] = sorted_A[i]
    # s의 최솟값 계산
    for i in range(n):
        s1 += new_A[i] * B[i]

    #print('A',new_A)
    #print('B', B)
    #print('s_A', sorted_A)
    #print('s_B', sorted_B)
    #print(s)
    print(s1)