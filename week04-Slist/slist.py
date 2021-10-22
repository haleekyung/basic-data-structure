class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link
    def __init__(self):
        self.head = None
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    # head 맨 앞에 item 삽입하기
    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
            # Node class 안에 있는 'item'으로 'item'이 할당, 'None'이 'link'에 할당되어 reference가 없는 것으로 정함

        else:
            self.head = self.Node(item, self.head) # 첫번째 또는 시작 노드
            # 첫번째 또는 시작 노드(self.head)를 Node(class)의 link에 할당

        self.size += 1 # size에 1을 추가함

    # 특정한 위치에 item 삽입하기
    def insert_after(self, item, p): # 위치를 변수 p로 할당
        p.next = self.Node(item, p.next)
        self.size += 1

    # 맨 앞에 있는 item 삭제하기
    def delete_front(self):
        # 앞에 아무것도 없는 경우 삭제 할 것 없으므로, 에러메세지 생성
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next # head를 head 다음에 있는 것으로 바꾸기
            self.size -= 1 # 끊긴 하나를 삭제함

    # 특정한 위치에 있는 item 삭제하기
    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError('Underflow')
        t = p.next
        p.next = t.next
        self.size -= 1

    # 타겟한 것 서치하기
    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.item: return k
            p = p.next # p를 next node로 바꾸겠다

        return None

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, '->', end='')

            else:
                print(p.item)
            p = p.next

class EmptyError(Exception):
    pass