class DynamicArray:
    def __init__(self, capacity: int):
        self.c = capacity
        self.a = []

    def get(self, i: int) -> int:
        return self.a[i]

    def set(self, i: int, n: int) -> None:
        self.a[i] = n

    def pushback(self, n: int) -> None:
        self.a.append(n)
        if len(self.a) > self.c:
            self.resize()

    def popback(self) -> int:
        return self.a.pop()
 
    def resize(self) -> None:
        self.c = 2 * self.c

    def getSize(self) -> int:
        return len(self.a)
    
    def getCapacity(self) -> int:
        return self.c