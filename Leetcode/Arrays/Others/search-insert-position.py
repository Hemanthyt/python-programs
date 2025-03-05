class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target == nums[mid]:
                return mid
            elif nums[mid]<= target:
                l=mid+1
            else:
                r=mid-1
        return l
s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5))
        