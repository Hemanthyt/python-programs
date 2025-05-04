class Solution:
    def FirstNegativeInteger(self, arr, k): 
        n=len(arr)
        res=[]
        for i in range(n-k+1):
            s=min(arr[i:i+k])
            if s<0:
                res.append(s)
            else:
                res.append(0)
        return res


s = Solution()
print(s.FirstNegativeInteger(arr = [-8, 2, 3, -6, 10] , k = 2))