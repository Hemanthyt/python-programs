class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        nums.append(nums[0])  # Append the first element to the end
        return max(abs(nums[i]-nums[i+1]) for i in range(len(nums)-1))
    
    
    
s = Solution()
print(s.maxAdjacentDistance(nums=[1,2,4]))
print(s.maxAdjacentDistance(nums=[-2,1,-5]))
print(s.maxAdjacentDistance(nums=[-5,-10,-5]))