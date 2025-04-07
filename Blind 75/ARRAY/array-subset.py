from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        x=Counter(a)
        y=Counter(b)
        for i in y:
            if y[i]>x[i]:
                return False
        return True
    
s = Solution()
print(s.isSubset(a = [11, 7, 1, 13, 21, 3, 7, 3], b = [11, 3,11, 7, 1, 7]))