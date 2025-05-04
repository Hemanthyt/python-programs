class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n=len(arr)
        res=[]
        for i in range(n-k+1):
            sett=set(arr[i:i+k])
            res.append(len(sett))
        return res
                
s = Solution()
print(s.countDistinct(arr= [1, 2, 1, 3, 4, 2, 3], k = 4))