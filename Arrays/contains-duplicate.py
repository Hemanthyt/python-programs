from collections import Counter
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        d=dict(Counter(nums))
        for  key,val in d.items():
            if val>1:
                return True
        return False

s = Solution()
print(s.hasDuplicate(nums= [1, 2, 3, 3]))