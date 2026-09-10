class LinkedList:

    def __init__(self):
        self.a = []
    
    def get(self, index: int) -> int:
        if index < len(self.a):
            return self.a[index]
        return -1

    def insertHead(self, val: int) -> None:
        self.a = [val] + self.a

    def insertTail(self, val: int) -> None:
        self.a.append(val)

    def remove(self, index: int) -> bool:
        if index < len(self.a):
            self.a = self.a[:index] + self.a[index + 1:]
            return True
        return False

    def getValues(self) -> List[int]:
        return self.a