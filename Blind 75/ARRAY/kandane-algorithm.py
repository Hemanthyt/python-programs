
class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        print(arr)
        res = float('-inf')
        sum=0
        for num in arr:
            sum+=num
            res=max(res,sum)
            if sum<0:
                sum=0
        return res
            
        
       
s = Solution()
print(s.maxSubArraySum( arr = [2, 3, -8, 7, -1, 2, 3]))
print(s.maxSubArraySum( arr = [-2,-4]))