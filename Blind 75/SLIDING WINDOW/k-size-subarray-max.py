class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        # code here
        n=len(arr)
        res=[]
        for i in range(n-k+1):
            s=max(arr[i:i+k])
            res.append(s)
            
        return res
s = Solution()
print(s.maxOfSubarrays([1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3))