import sys

sugar = int(sys.stdin.readline())
count = 0   # 봉지 개수
check = 0   # 나누기 가능 여부 확인

while sugar > 0:
    # 남은 설탕이 5의 배수이면 5kg 봉투로 모두 사용 바로 출력
    if sugar % 5 == 0:
        count += sugar//5
        check = 1
        break
    # 3kg 봉지 하나씩 사용 -> 3kg는 배수로 빼도 되지만 최소 개수를 쓰고 싶으니까 그냥 빼는 걸로
    else:
        sugar -= 3
        count += 1
        # 다 채울 수 있다면 종료조건
        if sugar == 0:
            check = 1

if check == 0:
    print(-1)
else:
    print(count)

