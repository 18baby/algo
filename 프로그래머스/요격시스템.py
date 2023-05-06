def solution(targets):
    answer = 0
    print(targets)
    targets.sort(key=lambda x:[x[1], x[0]])   # 끝 지점 기준 정렬
    print(targets)
    e = 0  # 초기 끝 지점
    for t in targets:
        if t[0] >= e:    # 새로운 시작지점이 기존의 끝 지점보다 크면 요격 불가!
            print(t)
            answer += 1  # 끝 지점 바로 앞에서 요격
            e = t[1]     # 끝 지점 업데이트
    return answer

print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))




