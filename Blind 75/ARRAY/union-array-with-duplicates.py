class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        a=set(a)
        b=set(b)
        c=a.union(b)
        return len(c)

s = Solution()
print(s.findUnion(a = [1, 2, 3, 4, 5], b = [1, 2, 3] ))