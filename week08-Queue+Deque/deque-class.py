from circularQueue import CircularQueue

MAX_QSIZE = 10

class CircularDeque(CircularQueue):
    def __init(self):
        super().__init__() # 부모클래스의 생성자를 호출함.

    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front -  1 # front를 앞으로 이동하겠다.
            if self.front < 0 : self.front = MAX_QSIZE - 1

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear];
            self.rear = self.rear - 1
            if self.rear < 0 : self.rear = MAX_QSIZE - 1
            return item

    def getRear(self): # 후단 peak
        return self.items[self.rear]

# test
dq = CircularDeque()
for i in range(9):
    if i % 2 == 0: dq.addRear(i)
    else: dq.addFront(i)

dq.display()
for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display()
for i in range(9, 14): dq.addFront(i)
dq.display()