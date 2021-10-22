# 스택의 응용 : 괄홈 검사하기
# 왼쪽 괄호는 스택에 push, 오른쪽 괄호는 읽으면 pop을 수행
# pop된 왼쪽 괄호와 바로 읽었던 오른쪽 괄호가 다른 종류이면 에러처리, 같은 종류이면 다음 괄호 읽음
# 모든 괄호를 읽은 뒤 에러가 없고 스택이 empty일 경우, 괄호들이 모두 정상적으로 사용된 것으로 간주
# 만일 모든 괄호를 처리한 후 스택이 empty가 아니면 짝이 맞지 않는 괄호가 스택에 남은 것이므로 에러처리

# 조건 1: 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다
# 조건 2: 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다
# 조건 3: 괄호 사이에는 포함 관계만 존재한다

# 잘못된 괄호 사용의 예
# 1: (a(b)
# 2: a(b)c)
# 3: a{b(c[d]e}f)

class Stack:
    def __init__(self):
        self.top = []

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

    def checkBrackets(statement):
        stack = Stack()
        for ch in statement:
            if ch in ('(', '[', '{'):
                stack.push(ch)
            elif ch in (')', ']', '{'):
                if stack.isEmpty():
                    return False
                else:
                    left = stack.pop()
                    if (ch == '}' and left != '{') or \
                       (ch == ')' and left != '(') or \
                       (ch == ']' and left != '['):
                        return False

        return stack.isEmpty()

