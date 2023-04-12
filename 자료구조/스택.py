# 스텍은 별도의 자료구조 필요 없음

class Stack:
    def __init__(self):
        self.container = []

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if self.empty():
            return None
        else:
            return self.container[-1]

