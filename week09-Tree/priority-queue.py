# 우선순위 큐 -> 정렬되지 않은 배열을 이용해 구현하

class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self): return len(self.items) == 0
    def size(self): return len(self.items)
    def clear(self): return self.items = []

    def findMaxIndex(self):
        if self.isEmpty(): return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i

                return highest

