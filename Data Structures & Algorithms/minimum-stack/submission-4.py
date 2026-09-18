class MinStack:

    def __init__(self):
        self.items = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.min_values or val <= self.min_values[-1]:
            self.min_values.append(val)


    def pop(self) -> None:

        item = self.items.pop()
        if self.min_values:
            if item == self.min_values[-1]:
                self.min_values.pop()
        return item

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min_values[-1] if self.min_values else 0

