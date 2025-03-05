class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        high=0
        sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sum+=nums[i]
            else:
                sum=nums[i]
            high=max(high,sum)            
        return high
            
            
s = Solution()
print(s.maxAscendingSum( nums=[10,20,30,5,10,50]))
print(s.maxAscendingSum( nums=[12,17,15,13,10,11,12]))