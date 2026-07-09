class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif self.minstack[-1] >= val:
            self.minstack.append(val)
        # print(self.stack, self.minstack)
        

        

    def pop(self) -> None:
        top = self.stack.pop()
        if self.minstack and self.minstack[-1] == top:
            self.minstack.pop()
        # print(self.stack, self.minstack)
        return top

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
