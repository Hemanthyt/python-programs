class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow,fast=0,0
        while True:
            # print(slow,fast)
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            print(slow,slow2)
            slow=nums[slow]
            slow2=nums[slow2]
            print(slow,slow2)
            if slow == slow2:
                break
        return slow
s = Solution()
print(s.findDuplicate(nums = [1,2,3,2,2]))
