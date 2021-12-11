class Chaining:
    class Node:
        def __init__(self, key, data, link):
            self.key = key
            self.data = data
            self.next = link

    def __init__(self, size):
        self.M = size
        self.a = [None] * size

    def hash(self, key):
        return key % self.M

    def put(self, data):
        key = self.hash(data)
        p = self.a[key]
        while p != None:
            if data == p.key:
                p.data = data
                return
            p = p.next
        self.a[key] = self.Node(key, data, self.a[key])

    def get(self, data):
        key = self.hash(data)
        p = self.a[key]
        result = 0
        while p != None:
            result += 1
            if data == p.data:
                return result
            p = p.next
        return 0

    def delete(self, data):
        key = self.hash(data)
        p = self.a[key]
        result = 0
        while p != None:
            result += 1
            if data == p.data:
                p = p.next
                return result
            p = p.next
        return 0

    def print(self):
        for i in range(self.M):
            p = self.a[i];
            while p != None:
                print(p.data, end=' ')
                p = p.next

if __name__ == "__main__":
    hash_size = int(input())
    ch = Chaining(hash_size)
    while True:
        str = input()
        inputValue = str.split(" ")
        if inputValue[0] == 'i':
            ch.put(int(inputValue[1]))

        elif inputValue[0] == 's':
            print(ch.get(int(inputValue[1])))

        elif inputValue[0] == 'd':
            print(ch.delete(int(inputValue[1])))

        elif inputValue[0] == 'p':
            ch.print()

        elif inputValue[0] == 'e':
            break