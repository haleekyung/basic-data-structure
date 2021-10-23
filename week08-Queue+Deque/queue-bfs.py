# queue class
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAZE_SIZE

    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1) % MAZE_SIZE

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAZE_SIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():                          # 공백상태가 아니면
            self.front = (self.front+1) % MAZE_SIZE     # front 회전
            return self.items[self.front]               # front 위치의 항목 변환

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % MAZE_SIZE]

    def size(self):
        return (self.rear - self.front + MAZE_SIZE) % MAZE_SIZE


# 너비우선탐색 : 깊이우선탐색과 알고리즘은 거의 같으나, 자료구조가 다름

def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'


def BFS():
    que = CircularQueue()
    que.enqueue((0, 1))
    print("BFS: ")

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end="->")
        x, y = here
        if (map[y][x] == 'x') : return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): que.enqueue((x, y - 1))  # 상
            if isValidPos(x, y + 1): que.enqueue((x, y + 1))  # 하
            if isValidPos(x - 1, y): que.enqueue((x - 1, y))  # 좌
            if isValidPos(x + 1, y): que.enqueue((x + 1, y))  # 우
    return False


# 테스트
map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1,' '1,' '0', '0', 'x'],
       ['1', '1', '1', '1', '1', '1']]

MAZE_SIZE = 6
result = BFS()
if result : print('--> 미로탐색 성공')
else : print('--> 미로탐색 실패')