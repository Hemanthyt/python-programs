class Solution:
    def isValid(self, s: str) -> bool:
        d={"(":")","{":"}","[":"]"}
        stack=[]
        for i in s:
            if i in d.keys():
                stack.append(i)
            else:
                if stack ==[]:
                    return 0
                else:
                    if d[stack[-1]]==i:
                        stack.pop()
                    else:
                        return False
        return stack==[]
s = Solution()
print(s.isValid(s = "([{}])"))
print(s.isValid(s = "[(])"))
