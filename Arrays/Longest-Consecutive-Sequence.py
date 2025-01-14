class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet=set(nums)
        long=0
        for num in nums:
            if num-1 not in numSet:
                length=1
                while num+length in numSet:
                    length+=1
                long=max(long,length)
        return long
s = Solution()
print(s.longestConsecutive(nums = [2,20,4,10,3,4,5]))
print(s.longestConsecutive(nums = [0,3,2,5,4,6,1,1]))
        