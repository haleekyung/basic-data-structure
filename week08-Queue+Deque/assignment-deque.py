from pycparser.c_ast import While


class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class Deque():
    def __init__(self, max_qsize):
        self.front = None
        self.rear = None
        self.max_qsize = max_qsize
        self.items = [None]

    def isEmpty(self): return self.front == None
    def isFull(self): return self.front == (self.rear + 1) % self.max_qsize
    def clear(self): self.front = self.front = None

    def add_front(self, x):
        node = DNode(x, None, self.front)
        if (self.isEmpty()):
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def add_rear(self, x):
        node = DNode(x, self.rear, None)
        if (self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def delete_front(self):
        While True:
            if not self.isEmpty():
                data = self.front.data
                self.front = self.front.next
                if self.front == None:
                    self.rear = None
                else:
                    self.front.prev = None
            else:
                print('underflow')
                break

    def delete_rear(self):
        While True:
            if not self.isEmpty():
                data = self.rear.data
                self.rear = self.rear.prev
                if self.rear == None:
                    self.front = None
                else:
                    self.rear.next = None
                return data
            else:
                print('underflow')
                break

    def print(self):
        for i in range(len[self.front], len[self.rear]):
            print(self.items[i], end='')


if __name__ == "__main__":
    deque = Deque(100)
    input_number = int(input())
    for number in range(input_number):
        input_string = input()
        operation = input_string.split(" ")
        if len(operation) == 1:
            if operation[0] == 'DF':
                deque.delete_front()

            elif operation[0] == 'DR':
                deque.delete_rear()

            elif operation[0] == 'P':
                deque.print()

        elif len(operation) == 2:
            if operation[0] == 'AF':
                deque.add_front(input())

            elif operation[0] == 'AR':
                deque.add_rear(input())