class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # stack=[]
        # res=[]
        # def backtrack(openN,closeN):
        #     print(stack,res)
        #     if openN == closeN == n:
        #         res.append("".join(stack))
        #         return
        #     if openN < n:
        #         stack.append("(")
        #         backtrack(openN+1,closeN)
        #         stack.pop()
        #     if closeN<openN:
        #         stack.append(")")
        #         backtrack(openN,closeN+1)
        #         stack.pop()
        # backtrack(0,0)
        # return res
        
        def dfs(left,right,s):
            if len(s)==n*2:
                res.append(s)
                return
            if left<n:
                dfs(left+1,right,s+"(")
            if right<left:
                dfs(left,right+1,s+")")
        res=[]
        dfs(0,0,"")
        return res
    
                
        
s = Solution()
print(s.generateParenthesis(n=3))