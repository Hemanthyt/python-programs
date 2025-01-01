class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            else:
                d[target-nums[i]]=i
        return False
        
            
        
s = Solution()
print(s.twoSum( nums=[-1,-2,-3,-4,-5], target = -8))
print(s.twoSum( nums = [4,5,6], target = 10))