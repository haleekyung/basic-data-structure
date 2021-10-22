class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self): return len(self.stack) == 0
    def size(self): return len(self.stack)
    def clear(self): self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop(-1)

    def peek(self):
        if self.isEmpty():
            print('Stack Empty')
        else:
            print(self.stack[-1])

    def pop(self):
        if self.isEmpty():
            print('Stack Empty')
        else:
            return self.stack.pop(-1)

    def duplicate(self):
        top = self.pop()
        for i in range(2):
            self.push(top)

    def upRotate(self, num):
        if num > self.size():
            return
        else:
            remain = self.size() - num
            temp = self.stack[remain:]
            top = temp[-1]
            for i in range(num-1, 0, -1):
                temp[i] = temp[i-1]
            temp[0] = top
            self.stack = self.stack[:remain] + temp


    def downRotate(self, num):
        if num > self.size():
            return

        else:
            remain = self.size() - num
            temp = self.stack[remain:]
            bottom = temp[0]
            for i in range(0, num-1):
                temp[i] = temp[i+1]
            temp[-1] = bottom
            self.stack = self.stack[:remain] + temp

    def print(self):
        len = self.size()
        for i in range(len-1, -1, -1):
            print(self.stack[i], end='')
        print()

if __name__ == "__main__":
    stack = Stack()
    while True:
        input_string = input()
        if input_string == "-1":
            print("프로그램 종료")
            break
        operation = input_string.split(" ")

        if len(operation) == 1:
            if operation[0] == "POP":
                stack.pop()

            elif operation[0] == "PEEK":
                stack.peek()

            elif operation[0] == "DUP":
                stack.duplicate()

            elif operation[0] == "PRINT":
                stack.print()

        elif len(operation) == 2:
            if operation[0] == "PUSH":
                stack.push(operation[1])

            elif operation[0] == "UpR":
                stack.upRotate(int(operation[1]))

            elif operation[0] == "DownR":
                stack.downRotate(int(operation[1]))