class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i != "../" and i != './':
                stack.append(i)
            if stack and i == "../":
                stack.pop()
        return len(stack)