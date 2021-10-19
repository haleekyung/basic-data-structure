class CircularQueue:
    def __init__(self, q_size):
        self.front = 0
        self.rear = 0
        self.q_size = q_size
        self.items = [None] * q_size

    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1) % self.q_size

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % self.q_size
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % self.q_size
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % self.q_size]

    def size(self):
        return (self.rear - self.front + self.q_size) % self.q_size

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]

        else:
            out = self.items[self.front+1:self.q_size] + self.items[0:self.rear+1]

        print("[f=%s, r=%d] ==>" %(self.front, self.rear), out)

q = CircularQueue(6)

q.enqueue(10)
q.enqueue(20)
q.display()
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.display()
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.display()