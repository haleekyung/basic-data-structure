class LinearProbing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size

    def hash(self, key):
        return key % self.M

    def put(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                # 주소 출력
                return

            if self.a[i] == key:
                return

            j += 1
            i = (initial_position + j) % self.M
            if i == initial_position:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + j) % self.M
            j += 1
            if i == initial_position:
                return

    def print(self):
        for i in range(self.M):
            print(str(self.a[i]), ' ', end= ' ')


# if __name__ == "__main__":
#     t = LinearProbing(13)
#     t.put(25, 'grape')
#     t.put(37, 'apple')
#     t.put(18, 'banana')
#     t.put(55, 'cherry')
#     t.put(22, 'mango')
#     t.put(35, 'lime')
#     t.put(50, 'orange')
#     t.put(63, 'watermelon')
#     t.print()


if __name__ == "__main__":
    M = int(input())
    linear = LinearProbing(M)
    str = input()
    inputValue = str.split( " " )
    while inputValue[0] != 'e':
        if inputValue[0] == 'i':
            linear.put(int(inputValue[1]))

        elif inputValue[0] == 's':
            linear.get(int(inputValue[1]))

        elif inputValue[0] == 'e':
            break