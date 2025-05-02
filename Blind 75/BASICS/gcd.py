class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,b%a)
        if b>a:
            a,b=b,a
        return gcd(a,b)
        

s = Solution()
print(s.gcd(a=3,b=6))