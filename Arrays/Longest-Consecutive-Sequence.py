class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in numSet:
                length=1
                while n+length in numSet:
                    length+=1
                longest = max(length,longest)
        return longest
s = Solution()
print(s.longestConsecutive(nums = [2,20,4,10,3,4,5]))
print(s.longestConsecutive(nums = [0,3,2,5,4,6,1,1]))
        