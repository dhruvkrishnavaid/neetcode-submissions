class MinStack:

    def __init__(self):
        self.stack = []
        self.minS = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minS or val <= self.minS[-1]:
            self.minS.append(val)

    def pop(self) -> None:
        s = self.stack.pop()
        if self.minS[-1] == s:
            self.minS.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minS[-1]