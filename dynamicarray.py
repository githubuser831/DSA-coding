class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:

        if self.length > 0:
            self.length -= 1

        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        transfer_arr = [0] * self.capacity

        for i in range(self.length):
            transfer_arr[i] = self.arr[i]
        self.arr = transfer_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
