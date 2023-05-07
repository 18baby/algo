
cap, n, deliveries, pickups = 4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]
#cap, n, deliveries, pickups = 2, 7,	[1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]

answer = 0   # 이동할 최단거리
d_index = n-1   # 배달 인덱스
p_index = n-1   # 수거 인덱스

while (deliveries[d_index] != 0) or (pickups[p_index] != 0):
    pickup = 0     # 회수할 상자수
    deliver = 0    # 배달할 상자수
    distance = []  # 트럭이 갈수 있는 최대 위치들 저장

    # (가장 멀리서 부터 확인)
    # *** 배송 ***
    for i in range(d_index, -1, -1):
        deliver += deliveries[i]
        if deliver > cap:  # 배송 불가 -> 배송 가능 개수 초과
            deliveries[i] = deliver - cap
            distance.append(i)
            break
        else:  # 배송 가능
            deliveries[i] = 0
            d_index -= 1   # 다음 최대 배송 거리 저장
            distance.append(i)
    print(f"배송 상태: {deliveries}")

    # *** 회수 ***
    for i in range(p_index, -1, -1):
        pickup += pickups[i]
        if pickup > cap:  # 수거 불가
            pickups[i] = pickup - cap
            distance.append(i)
            break
        else:
            pickups[i] = 0
            p_index -= 1  # 다음 최대 회수거리 저장
            distance.append(i)
    print(f"회수 상태: {pickups}")

    if distance:
        answer += (max(distance)+1)*2    # 이동 거리
    print(f"최대 거리: {distance}, answer: {answer}")
    print(d_index, p_index)
print(answer)
