class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        folders = [f for f in path.split("/") if f]
        for folder in folders:
            if folder == "..":
                if stack:
                    stack.pop()
            elif folder != ".":
                stack.append(folder)
        
        return "/"+ "/".join(stack)
        