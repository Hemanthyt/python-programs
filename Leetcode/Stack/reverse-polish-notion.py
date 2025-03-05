class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        d=["+","-","*","/"]
        stack=[]
        for i in tokens:
            if i not in d:
                stack.append(int(i))
            else:
                if i =="+":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a+b)
                elif i =="-":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b-a)
                elif i =="*":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a*b)
                elif i =="/":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(float(b)/a))
        return stack[0]
                
                
            
        
s = Solution()
print(s.evalRPN(tokens = ["1","2","+","3","*","4","-"]))