class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            if self.minstack and val <= self.minstack[-1]:
                self.minstack.append(val)
        

    def pop(self) -> None:
        top = self.stack.pop()
        if self.minstack[-1] == top:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
