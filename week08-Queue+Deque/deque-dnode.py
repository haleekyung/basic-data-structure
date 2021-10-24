class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoubleLinkedDeque:
    def __init__(self):
        self.front = None # 초기화이면서, 구현을 위한 생성자
        self.rear = None

    def isEmpty(self): return self.front == None
    def clear(self): return self.front == None
    def size(self): return self.size # 수정

    def addFront(self, item):
        node = DNode(item, None, self.front)    # step 1
        if self.isEmpty():
            self.front = self.rear = node
        else:                                   # step 2
            self.front.prev = node
            self.front = node                   # step 3

    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear == None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front == None
            else:
                self.rear.next = None
            return data


dq = DoubleLinkedDeque()

dq.addFront(10)
