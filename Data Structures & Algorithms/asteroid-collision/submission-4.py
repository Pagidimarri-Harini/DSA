class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        noinsert = False
        for i in asteroids:
            # print(stack)

            while stack and stack[-1] > 0 and i < 0 and stack[-1] < abs(i):
                stack.pop()

            if stack and i < 0 and stack[-1] >= abs(i):
                if stack[-1] == abs(i):
                    stack.pop()
                noinsert = True 
            if not noinsert:
                stack.append(i)
            noinsert = False


                
            
            
        return stack

        