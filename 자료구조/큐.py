class Queue:
    def __init__(self):
        self.contanier = []

    def empty(self):
        if not self.contanier:
            return True
        else:
            return False

    def enqueue(self, data):
        self.contanier.append()

    def dequeue(self):
        return self.contanier.pop(0)

    def peek(self):
        return self.contanier[0]
    
# 라이브러리 이용 -> 덱 라이브러리 (덱에선 일반적인 인덱싱, 슬라이싱은 사용 불가)
from collections import deque

data = deque([2, 3, 4])
data.append(5)       # 가장 마지막에 데이터 추가
data.appendleft(1)   # 가장 앞에 데이터 추가

print(data)
print(list(data))
 
data.pop()          # 가장 마지막의 데이터 추출
print(data)
data.popleft()      # 가장 앞의 데이터 추출

print(data)
print(list(data))