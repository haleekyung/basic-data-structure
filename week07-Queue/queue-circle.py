## 수업에서 사용된 코드

# 큐 사이즈를 10으로 지정함
MAX_QSIZE = 10

# 큐 클래스 작성
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1) % MAX_QSIZE

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():                          # 공백상태가 아니면
            self.front = (self.front+1) % MAX_QSIZE     # front 회전
            return self.items[self.front]               # front 위치의 항목 변환

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % MAX_QSIZE]

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE