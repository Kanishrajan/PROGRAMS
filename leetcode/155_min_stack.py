class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st or val <= self.min_st[-1]:
            self.min_st.append(val)

    def pop(self) -> None:
        if not self.st:
            return

        x = self.st.pop()

        if self.min_st and x == self.min_st[-1]:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]


if __name__ == "__main__":

    obj = MinStack()

    obj.push(-2)
    obj.push(0)
    obj.push(-3)

    print("getMin() =", obj.getMin())  # -3

    obj.pop()

    print("top() =", obj.top())        # 0
    print("getMin() =", obj.getMin())  # -2

    print("-" * 40)

    obj.push(-5)

    print("top() =", obj.top())        # -5
    print("getMin() =", obj.getMin())  # -5
