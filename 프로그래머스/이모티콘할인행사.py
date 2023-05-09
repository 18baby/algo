
users, emoticons = [[40, 10000], [25, 10000]], [7000, 9000]
#users, emoticons = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]

answer = []
print(users)

n = len(users)      # 사람수
m = len(emoticons)  # 이모티콘 수
m_price = [0]*n     # 사람별 구매 이모티콘 금액
plus = 0            # 이모티콘 플러스 가입자수
sales = [0.1, 0.2, 0.3, 0.4]  # 가능한 할인율

# 사람 기준으로 생각
for i in range(n):
    print(f"{i+1}번째 고객 -> 할인률 하한:{users[i][0]/100}, 구매상한: {users[i][1]}")
    price = 0   # 사람별 이모티콘 구매 총 금액
    # 이모티콘 종류별 확인
    for j in range(m):
        m_total = 0  # 이모티콘별 구매 가능 최대 금액 저장
        # 할인률 바꾸면서 확인
        for sale in sales:
            if users[i][0]/100 <= sale:   # 구매 조건 성립
                print(f"할인률{sale}에서 {j+1}번째 이모티콘 구매")
                p = emoticons[j]*(1-sale)    # j번째 이모티콘 sale%로 구매
                print(f"{j+1}번째 이모티콘 수익: {p}")
                break
        price += p    # 이모티콘 구매 총 금액 업데이트
        print(f"구매 금액: {price}")
        # 플러스 가입 조건 충족시
        if price >= users[i][1]:
            print("가입 성공!")
            plus += 1
            price = 0
            break
    m_price[i] = price     # i번째 사람의 최종 구매 금액
    print(m_price)
    print()
    
print(m_price)
print(plus)
print(sum(m_price))

