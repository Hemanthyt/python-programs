class Solution:
    def subarraySum(self, arr, target):
        # code here
        l=0
        res=0
        for r in range(len(arr)):
            res+=arr[r]
            if res==target:
                return [l+1,r+1]
            elif res>target:
                while l<=r and res>target:
                    res-=arr[l]
                    l+=1
        