
class Solution:
    def evenlyDivides(self, n):
        # code here
        if n==0:
            return 0
        count=0
        for i in str(n):
            if int(i)!=0 and n!=0 and n%int(i) ==0:
                count+=1
        return count

s = Solution()
print(s.evenlyDivides(n=2406))
print(s.evenlyDivides(n=0))