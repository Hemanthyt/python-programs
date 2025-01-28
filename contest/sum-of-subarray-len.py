class Solution(object):
    def subarraySum(self, nums):
        total_sum = 0
        n = len(nums)
        
        for i in range(n):
            # Define the start of the subarray
            start = max(0, i - nums[i])
            # Sum the subarray from start to i
            total_sum += sum(nums[start:i + 1])
        
        return total_sum

s = Solution()
print(s.subarraySum( nums = [3,1,1,2]))