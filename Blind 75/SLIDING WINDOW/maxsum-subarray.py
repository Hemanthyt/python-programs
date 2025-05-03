class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here 
        n=len(arr)
        sum=0
        for i in range(k):
            sum+=arr[i]
        res=sum
        for i in range(k,n):
            sum+=arr[i]
            sum-=arr[i-k]
            res=max(res,sum)
        return res
                
s = Solution()
print(s.maximumSumSubarray(arr = [100, 200, 300, 400] , k = 2))
print(s.maximumSumSubarray(arr = [100, 200, 300, 400] , k = 4))