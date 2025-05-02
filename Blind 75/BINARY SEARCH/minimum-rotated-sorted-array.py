class Solution:
    def findMin(self, nums: list[int]) -> int:
        curr_min=float("infinity")
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            curr_min=min(curr_min,nums[mid])
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
        return curr_min
        
s = Solution()
print(s.findMin( nums = [4,5,6,7,0,1,2]))