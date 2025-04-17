class Solution:

    def kthElement(self, a, b, k):
        c=a+b
        c.sort()
        print(c)
        return c[k-1]
s = Solution()
print(s.kthElement(a = [2, 3, 6, 7, 9], b = [11,1,1,1, 4, 8, 10], k = 5 ))