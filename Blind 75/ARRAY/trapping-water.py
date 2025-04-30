class Solution:
    def maxWater(self, arr):
        # code here
        l,r=0,len(arr)-1
        lmax,rmax=0,0
        trapwater=0
        while l<r:
            lmax=max(lmax,arr[l])
            rmax = max(rmax,arr[r])
            
            if lmax<=rmax:
                trapwater+=lmax-arr[l]
                l+=1
            else:
                trapwater+=rmax-arr[r]
                r-=1
        return trapwater
                
                

s = Solution()
print(s.maxWater( arr = [3, 0, 1, 0, 4, 0, 2]))