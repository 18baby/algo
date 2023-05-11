
# 문자열 압축 함수
def compression(s, k):
    n = len(s)
    result = s[:k]   # 결과 문자열
    #print(s)

    pre_i = 0         # 초기 이전 단어 시작 인덱스
    pre_word = s[:k]  # 초기 이전 단어
    count = 1         # 단어 반복 횟수
    # 단어들 돌면서 확인
    for i in range(k, n, k):
        # 현재 확인할 단어
        if i+k <= n:
            now_word = s[i:i+k]
        else:
            now_word = s[i:]
        print(f"이전 단어({pre_i}~{i}): {pre_word}, 현재 단어({i}~{i + k}): {now_word}, 현재 단어 길이: {len(now_word)}")
        # 이전 단어와 현재 단어가 같은 경우
        if pre_word == now_word:
            count += 1     # 같은 단어면 횟수 증가
            if count > 2:  # 숫자 변경
                if result[-2:].isdigit():   # count가 두자리수일때
                    result = list(result)
                    result[-2] = str(count//10)
                    result[-1] = str(count%10)
                elif result[-1].isdigit():  # count가 한자리수일때
                    result = list(result)
                    result[-1] = str(count)
                result = ''.join(result)
            else:          # 숫자 생성
                result += str(count)
        else:
            count = 1
            result += now_word

        pre_i = i
        pre_word = now_word
        print(result)

    print(f"최종: {result}")
    return len(result)


# 문제 함수 -> 압축표현이 가장 짧은 것의 길이 구하기
def solution(s):
    n = len(s)
    # 테스트케이스 5번 오류 방지
    if n == 1:
        return 1
    answer = 1000
    # 하나씩 확인하면서 최소값 탐색
    for k in range(1, n):
        result = compression(s, k)
        print(f"{k}일때 {result}")
        answer = min(answer, result)   # 최솟값 갱신

    return answer


print(solution("aabbaccc"))
#print(solution("ababcdcdababcdcd"))
#print(solution("abcabcdede"))
#print(solution("abcabcabcabcdededededede"))
#print(solution("xababcdcdababcdcd"))
