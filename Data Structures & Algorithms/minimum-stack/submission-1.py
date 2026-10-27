class MinStack:

    def __init__(self):
        self.Stack = []

    def push(self, val: int) -> None:
        if self.Stack:
            current_min = min(val, self.Stack[-1][1])
        else:
            current_min = val

        self.Stack.append((val, current_min))

    def pop(self) -> None:
        self.Stack.pop()

    def top(self) -> int:
        return self.Stack[-1][0]

    def getMin(self) -> int:
        return self.Stack[-1][1]