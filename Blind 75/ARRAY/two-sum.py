from collections import Counter
class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def twoSum(self, arr, target):
            d={}
            for i in arr:
                if i in d:
                    return True
                else:
                    d[target-i]=i
            return False
      
        

        
s = Solution()
print(s.twoSum(arr = [1, 4, 45, 8, 10, 8], target = 16))
print(s.twoSum(arr =[1, 2, 4, 3, 6], target = 11))
# print(s.twoSum(arr = [1, 4, 45, 8, 10, 8], target = 16))