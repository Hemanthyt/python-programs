class Solution:
    def getLastDigit(self, a, b):
        a=int(a)
        b=int(b)
        if a==0 and b==0:
            return 1
        if a==0:
            return 0
        if b==0:
            return 1
        # If exponent is tooo big it takes more time to make
        # power so use simple approch og exp%4 so that can easily get the last num
        
        if b%4==0:
            res = 4
        else:
            res = b%4
        
        num = pow(a,b)
        return num%10
        
s = Solution()
print(s.getLastDigit(a = "3", b = "10"))
print(s.getLastDigit(a = "6", b = "2"))