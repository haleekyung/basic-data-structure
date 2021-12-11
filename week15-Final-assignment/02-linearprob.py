class LinearProbing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size

    def hash(self, key):
        return key % self.M

    def put(self, data):
        initial_position = self.hash(data)
        i = initial_position
        j = 0
        conflict = ""
        while True:
            if self.a[i] == None:
                self.a[i] = data
                return conflict + str(i)
            if self.a[i] == data:
                return i

            conflict += "C"
            j += 1
            i = (initial_position + j) % self.M
            if i == initial_position:
                return -1

    def get(self, data):
        initial_position = self.hash(data)
        i = initial_position
        j = 0
        while self.a[i] != None:
            if self.a[i] == data:
                return str(i) + " " + str(data)
            i = (initial_position + j) % self.M
            j += 1
            if i == initial_position:
                return -1
        return -1

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
    while True:
        inputs = input()
        inputValue = inputs.split( " " )
        if inputValue[0] == 'i':
            print(linear.put(int(inputValue[1])))

        elif inputValue[0] == 's':
            print(linear.get(int(inputValue[1])))

        elif inputValue[0] == 'e':
            break

# 입력 예시 1
# if __name__ == "__main__":
#     linear = LinearProbing(7)
#     print(linear.put(17011112))
#     print(linear.put(17012345))
#     print(linear.put(17012687))
#     print(linear.get(17011111))

# 입력 예시 2
# if __name__ == "__main__":
#     linear = LinearProbing(13)
#     print(linear.put(16110243))
#     print(linear.put(17011111))
#     print(linear.put(17012331))
#     print(linear.put(17012354))
#     print(linear.put(17013672))
#     print(linear.put(16012342))
#     print(linear.get(17012354))
#     print(linear.put(15013986))
#     print(linear.put(102067))
#     print(linear.put(113478))
#     print(linear.put(14012322))
#     print(linear.get(16110243))

