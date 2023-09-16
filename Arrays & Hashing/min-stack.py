#https://leetcode.com/problems/min-stack/
Class MinStack:

    def __init__(self):
        self.data = []
        self.size = 0
        self.min = []

    def push(self, val: int) -> None:
        self.data.append(val)
        self.size = self.size + 1

        if self.min == []:
            self.min = [val]
        elif val <= self.min[-1]:
            self.min.append(val)


    def pop(self) -> None:
        if self.min[-1] == self.data[-1]:
            self.min.pop()

        self.data.pop()

        self.size = self.size - 1

    def top(self) -> int:
        return self.data[self.size - 1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()