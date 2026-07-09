class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = 1
        tempcount = 0
        for i in s:
            # print(stack)
            if tempcount == k:
                while stack and tempcount > 0:
                    stack.pop()
                    tempcount -= 1
            if stack and i == stack[-1][0]:
                count = stack[-1][1] + 1
            else:
                count = 1
            stack.append((i, count))
            tempcount = stack[-1][1]
        
        if tempcount == k:
            while stack and tempcount > 0:
                stack.pop()
                tempcount -= 1
            
        return ''.join([i[0] for i in stack])

        