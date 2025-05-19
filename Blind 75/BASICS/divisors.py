class Solution:
    def divisors(self, n):
        res=[]
        for i in range(1,n//2+1):
            if n % i == 0:
                res.append(i)
        res.append(n)
        return res
  
                
s = Solution()
print(s.divisors(n=12))