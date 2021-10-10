# 단순연결리스트로 구현한 스택

# Node 클래스 만들기 (함수 만들기와 같으나 class만 더 들어갔다는 점에서 차이 있음)
class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link

def push(item):
    global top  # 전역변수 선언
    global size # 전역변수 선언

    top = Node(item, top)
    size += 1

def peek():
    if size != 0:
        return top.item

def pop():
    global top
    global size
    if size != 0:
        top_item = top.item
        top = top.next
        size -= 1

        return top_item # 제거된 top 항목 리턴

def print_stack():
    print('top -> \t', end='')
    p = top
    while p:
        if p.next != None:
            print(p.item, '-> ', end='')
        else:
            print(p.item, end='')
        p = p.next
    print()

top = None
size = 0

# 실행하기
push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후: \t', end='')
print_stack()

print('top항목: ', end='')
print(peek())

push('pear')
print('배 push 후: \t\t', end='')
print_stack()

pop()

push('grape')
print('pop(), 포도 push 후:\t', end='')
print_stack()
