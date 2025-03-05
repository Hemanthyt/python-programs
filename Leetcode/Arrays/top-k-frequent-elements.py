from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result=dict(Counter(nums))
        result = dict(sorted(result.items(), key=lambda item: item[1]))
        return list(result.keys())[-k:]
s = Solution()
print(s.topKFrequent( nums = [1,2,2,2,3,3,3,3], k = 2))