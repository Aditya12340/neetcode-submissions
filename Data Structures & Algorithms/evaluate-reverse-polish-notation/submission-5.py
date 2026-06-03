class Solution:
    def num(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        if n == 0:
            return 0
        elif  n == 1: 
            return int(tokens[0])
        
        store = []
        temp = 0

        for i in range(n): 
            temp = tokens[i]
            if self.num(temp) == True: 
                store.append(int(temp))
            elif tokens[i] == "+":
                b, a = store.pop(), store.pop()
                store.append(a + b)
            elif tokens[i] == "-":
                b, a = store.pop(), store.pop()
                store.append(a - b)
            elif tokens[i] == "*":
                store.append(store.pop() * store.pop())
            elif tokens[i] == "/":
                b, a = store.pop(), store.pop()
                store.append(int(a / b))
            
        return int(store[0])
