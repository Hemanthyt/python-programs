class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        a.sort()
        b.sort()
        print(a,b)
        return a == b
s = Solution()
print(s.checkEqual(a = [1, 2, 4, 4, 0], b = [2, 4, 5, 0, 1]))