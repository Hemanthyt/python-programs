class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r=0,len(nums)-1
        cur_min=float("inf")
        while l<=r:
            mid = (l + r) // 2
            cur_min = min(cur_min,nums[mid])
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
        return cur_min

s = Solution()
print(s.minEatingSpeed(nums = [3,4,5,6,1,2]))
        