import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            mid = (l+r)//2
            totalTime=0
            for p in piles:
                totalTime+= math.ceil(p / mid)
            if totalTime<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res

        
s = Solution()
print(s.minEatingSpeed( piles = [3,6,7,11], h = 8))