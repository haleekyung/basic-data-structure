class Stack:
    def __init__(self):
        self.top = []
        self.bracket_num = 0

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

    def addBracketNumber(self):
        self.bracket_num += 1

    def printOutput(self, test_case):
        if self.checkBrackets( test_case ):
            print( 'OK_' + format( self.bracket_num ) )
        else:
            print( 'Wrong_' + format( self.bracket_num ) )

    def checkBrackets(self, statement):
        self.top = []
        self.bracket_num = 0
        for ch in statement:
            if ch in ('(', '[', '{'):
                self.push(ch)
                self.addBracketNumber()
            elif ch in (')', ']', '}'):
                self.addBracketNumber()
                if self.isEmpty():
                    return False
                else:
                    left = self.pop()
                    if (ch == '}' and left != '{') or (ch == ')' and left != '(') or (ch == ']' and left != '['):
                        return False

        return self.isEmpty()

stack = Stack()

for i in range(0, 4):
    test_case = input()
    stack.printOutput(test_case)