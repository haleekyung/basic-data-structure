class DoubleHashing:
    def __init__(self, size, q):
        self.M = size
        self.a = [None] * size
        self.q = q
        self.N = 0

    def hash(self, key):
        return key % self.M

    def doubleHash(self, key):
        return self.q - (key % self.q)

    def put(self, key):
        initial_position = self.hash(key)
        i = initial_position
        d = self.doubleHash(key)
        j = 0
        conflict = ""
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.N += 1
                return conflict + str(i)

            if self.a[i] == key:
                return -1

            conflict += "C"
            j += 1
            i = (initial_position + j * d) % self.M
            if self.N > self.M:
                return -1

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        d = self.doubleHash(key)
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return str(i) + " " + str(key)
            j += 1
            i = (initial_position + j * d) % self.M
        return -1

    def print(self):
        for i in range(self.M):
            if self.a[i] == None:
                print(0, end=' ')
            else:
                print(str(self.a[i]), end=' ')
        print()
if __name__ == "__main__":
    inputs = input()
    M = int(inputs.split(" ")[0])
    q = int(inputs.split(" ")[1])
    double = DoubleHashing(M, q)
    while True:
        inputs = input()
        inputValue = inputs.split(" ")
        if inputValue[0] == 'i':
            print(double.put(int(inputValue[1])))

        elif inputValue[0] == 's':
            print(double.get(int(inputValue[1])))

        elif inputValue[0] == 'p':
            double.print()

        elif inputValue[0] == 'e':
            double.print()
            break

# if __name__ == "__main__":
#     doubleHash = DoubleHashing(13,11)
#     print(doubleHash.put(25))
#     print(doubleHash.put(13))
#     print(doubleHash.put(16))
#     print(doubleHash.put(15))
#     print(doubleHash.put(70))
#     doubleHash.print()
#     print(doubleHash.put(28))
#     print(doubleHash.put(31))
#     print(doubleHash.put(20))
#     print(doubleHash.put(14))
#     print(doubleHash.get(20))
#     print(doubleHash.get(27))
#     print(doubleHash.put(38))
#     doubleHash.print()