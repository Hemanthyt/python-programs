class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        answers=[0]*len(temperatures)
        
        for idx,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                popTemp,popIdx=stack.pop()
                answers[popIdx]=idx-popIdx
            stack.append((temp,idx))
        return answers
s = Solution()
print(s.dailyTemperatures(temperatures = [30,38,30,36,35,40,28]))
        