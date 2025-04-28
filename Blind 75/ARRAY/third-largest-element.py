class Solution:
    def thirdLargest(self,arr):
        # code here
        if len(arr) >=3:
            arr.sort(reverse = True)
            return arr[2]
        else:
            return -1
s = Solution()
print(s.thirdLargest(arr=[3, 2, 1, 56, 10000, 167]))