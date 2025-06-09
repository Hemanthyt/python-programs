class Solution:
    def armstrongNumber (self, n):
        # code here 
        amstrong =0
        for i in str(n):
            amstrong += int(i)**3
        return n==amstrong


s = Solution()
print(s.armstrongNumber(n=153))
print(s.armstrongNumber(n=328))