class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        count=0
        # sum=0
        # d={0:1}
        # for num in arr:
        #     sum+=num
        #     if (sum-k) in d:
        #         count+=d[sum-k]
        #     if sum in d:
        #         d[sum]+=1
        #     else:
        #         d[sum]=1
        # return count
        
        res=0
        d={}
        sum=0
        
        for i in range(len(arr)):
            sum+=arr[i]
            
            if sum == k:
                res = i+1
            elif(sum-k) in d:
                res = max(res, i-d[sum-k])
                
            if sum not in d:
                d[sum] = i
        return res
        
        
        
        
s = Solution()
print(s.longestSubarray(arr = [10, 5, 2, 7, 1, -10], k = 15))
    