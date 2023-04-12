
# 가지고 있는 동전 500원, 100원, 50원, 10원 (무한이 많음)
N = int(input('거스름돈 입역'))
count = 0

while N != 0:
    if N >= 500:
        N -= 500
        count += 1

    elif N >= 100:
        N -= 100
        count += 1

    elif N >= 50:
        N -= 50
        count += 1

    elif N >= 10:
        N -= 10
        count += 1

print(f'필요한 최소 동전개수: {count}')

# 교재 코드 (훨신 깔끔)
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += N // coin
    N %= coin

print(count)
