from week06.practiceCheckBrackets import Stack

map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1,' '1,' '0', '0', 'x'],
       ['1', '1', '1', '1', '1', '1']]

MAZE_SIZE = 6

def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def DFS():
    stack = Stack()
    stack.push((0, 1))
    print("DFS: ")

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end='')
        (x, y) = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): stack.push((x, y - 1)) # 상
            if isValidPos(x, y + 1): stack.push((x, y + 1))  # 하
            if isValidPos(x - 1, y): stack.push((x - 1, y))  # 좌
            if isValidPos(x + 1, y): stack.push((x + 1, y))  # 우

        print('현재 스택: ', stack.pop)

    return False


result = DFS()
if result : print('--> 미로탐색 성공')
else : print('--> 미로탐색 실패')