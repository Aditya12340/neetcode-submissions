class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack [] that tracks all the 
        stack = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c) 
            if c == ')' or c == ']' or c == '}':
                if len(stack) != 0 and stack[-1] == matching[c]:        
                    stack.pop()
                else: 
                    return False
        
        if len(stack) == 0: 
            return True
        else: 
            return False







            


        