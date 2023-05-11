def solution(book_time):
    answer = 1
    n = len(book_time)

    # 예약 1개만 있을때
    if n == 1:
        return answer

    # 예약시간 수치로 변경
    for i in range(n):
        start, end = book_time[i][0], book_time[i][1]
        s_h, s_m = map(int, start.split(":"))
        e_h, e_m = map(int, end.split(":"))
        # 시간 -> (시.분) 형태로 변경
        start = s_h*60 + s_m
        end = e_h*60 + e_m + 10    # 퇴실 시간에 청소시간 포함
        book_time[i] = [start, end]
    #print(book_time)

    # 퇴실 시간 기준 정렬
    book_time.sort(key=lambda x: x[1])
    print(book_time)

    # 예약 가능 방 확인
    min_check_out = book_time[0][1]  # 최초 체크아웃 시간
    for i in range(1, n):
        print(f"새로운 시작시간:{book_time[i][0]}, 가장 가까운 퇴실 시간:{min_check_out}")
        # 새로운 방 추가 경우
        if book_time[i][0] < min_check_out:
            answer += 1
            print(f"{i}번째에서 방추가")
        min_check_out = min(min_check_out, book_time[i][1])  # 가장 빠른 퇴실 시간 체크

    return answer


#print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
#print()
#print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
#print()
#print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))


# 힙 이용 방법(다른사람 코드)
from heapq import heappop, heappush

def solution(book_time):
    answer = 1
    n = len(book_time)

    # 예약 1개만 있을때
    if n == 1:
        return answer

    # 예약시간 수치로 변경
    for i in range(n):
        start, end = book_time[i][0], book_time[i][1]
        s_h, s_m = map(int, start.split(":"))
        e_h, e_m = map(int, end.split(":"))
        # 시간 -> (시.분) 형태로 변경
        start = s_h * 60 + s_m
        end = e_h * 60 + e_m + 10   # 퇴실 시간에 청소시간 포함
        book_time[i] = [start, end]
    # print(book_time)

    # 입실 시간 기준 정렬
    book_time.sort(key=lambda x: x[0])
    print(f"정렬된 예약 시간: {book_time}")

    room = []   # 채워진 방 개수
    for start, end in book_time:
        # 모든 방이 비었으면 방 추가
        if not room:
            heappush(room, end)
            continue
        # 방이 비면 새로운 손님 받음
        if room[0] <= start:
            heappop(room)
        # 새로운 방 추가
        else:
            answer += 1
        heappush(room, end)
        print(f"room 상태{room}")

    return answer


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print()
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print()
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))