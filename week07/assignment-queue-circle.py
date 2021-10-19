# 큐 사이즈 정의
q_size = int(input())

# 큐 클래스 작성
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * q_size

    def qSize(self):
        size = int(input())
        return self.q_size

    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1) % self.q_size

    def enqueue(self, items):
        if not self.isEmpty():
            self.rear = (self.rear+1) % self.q_size
            self.items[self.rear] = self.items

    def dequeue(self):
        if not self.isEmpty():                                # 공백상태가 아니면
            self.front = (self.front+1) % self.q_size     # front 회전
            self.front[-1] = None
            return self.items[self.front]                 # front 위치의 항목 변환

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % self.q_size]

    def size(self):
        return (self.rear - self.front + self.q_size) % self.q_size

    def print(self):
        for i in range(len(self.items)):
            print(self.items[i])
        print()


if __name__ == "__main__":
    cq = CircularQueue
    input_number = int(input())
    for number in range(input_number):
        input_string = input()
        operation = input_string.split(" ")
        if len(operation) == 1:
            if operation[0] == 'D':
                cq.dequeue()

            elif operation[0] == 'P':
                cq.print()

        elif len(operation) == 2:
            if operation[0] == "I":
                cq.enqueue(input())