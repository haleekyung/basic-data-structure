class LinearProbing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size

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
            print(str(self.a[i]), end=' ')


if __name__ == "__main__":
    M = int(input())
    linear = LinearProbing(M)
    while True:
        inputs = input()
        inputValue = inputs.split(" ")
        if inputValue[0] == 'i':
            print(linear.put(int(inputValue[1])))

        elif inputValue[0] == 's':
            print(linear.get(int(inputValue[1])))

        elif inputValue[0] == 'e':
            break