class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l,r=0,len(heights)-1
        res=0
        while l<r:
            d=r-l
            m = min(heights[l],heights[r])
            f=d*m
            if f>res:
                res=f
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return res
            
        
s = Solution()
print(s.maxArea(heights = [1,7,2,5,4,7,3,6]))