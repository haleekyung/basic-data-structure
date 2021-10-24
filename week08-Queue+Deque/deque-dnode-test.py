class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.size = 0
        self.front = None # 초기화이면서, 구현을 위한 생성자
        self.rear = None

    def isEmpty(self): return self.front == None
    def clear(self): self.front = self.front = None

    def add_size(self):
        self.size += 1

    def delete_size(self):
        self.size -= 1

    def add_front(self, x):
        self.add_size()
        node = DNode(x, None, self.front)    # step 1
        if self.isEmpty():
            self.front = self.rear = node
        else:                                   # step 2
            self.front.prev = node
            self.front = node                   # step 3

    def add_rear(self, x):
        self.add_size()
        node = DNode(x, self.rear, None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def delete_front(self):
        self.delete_size()
        while True:
            if not self.isEmpty():
                data = self.front.data
                self.front = self.front.next
                if self.front == None:
                    self.rear == None
                else:
                    self.front.prev = None
                return data
            else:
                print('underflow')
                break

    def delete_rear(self):
        self.delete_size()
        while True:
            if not self.isEmpty():
                data = self.rear.data
                self.rear = self.rear.prev
                if self.rear == None:
                    self.front == None
                else:
                    self.rear.next = None
                return data
            else:
                print('underflow')
                break

    def print(self):
        for elem in range(self.size):
            print(self.front.next, end='')

    def print_list(self):
        if self.isEmpty():
            return;

        p = self.front
        while p:
            if p.next != None:
                print(p.data, end=' ')

            else:
                print(p.data, '\n')
            p = p.next

if __name__ == "__main__":
    deque = Deque()
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
                deque.print_list()

        elif len(operation) == 2:
            if operation[0] == 'AF':
                deque.add_front(operation[1])

            elif operation[0] == 'AR':
                deque.add_rear(operation[1])