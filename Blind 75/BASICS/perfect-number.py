class Solution:
    def divisors(self, n):
        res=1
        for i in range(2,n//2+1):
            if n % i == 0:
                res+=i
        return res ==n

                
s = Solution()
print(s.divisors(n=6))