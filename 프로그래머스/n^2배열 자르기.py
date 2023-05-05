n, left, right = 3, 2, 5

# 시간 초과 코드
def solution(n, left, right):
    # 2차원 배열 생성
    mat = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                mat[i][j] = j+1
            else:
                mat[i][j] = i+1
    # 차원 축소
    arr = []
    for i in range(n):
        arr = arr + mat[i]
    # 최종 배열 추출
    answer = arr[left:right+1]
    return answer

# 직접 정답 코드 생성(내코드)
def solution2(n, left, right):
    l = right - left + 1  # 정답 리스트 길이
    answer = [0]*l        # 정답 리스트
    for i in range(l):
        index = i + left  # 현재 인덱스
        row = index // n  # 2차원 배열에서의 행 위치
        col = index % n   # 2차원 배열에서의 열 위치
        # 정답 배열 채우기
        if row <= col:
            answer[i] = col + 1
        else:
            answer[i] = row + 1
    return answer

print(solution2(4, 7, 14))


# 다른 사람 코드
def solution3(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)
    return answer