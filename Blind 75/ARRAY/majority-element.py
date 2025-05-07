from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        count = Counter(nums)
        for num,val in count.items():
            if val > len(nums)/2:
                return val
        
