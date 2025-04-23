class Solution:
    def missingNumber(self, arr):
        # code here
        arr.sort()
        for i in range(len(arr)):
            if i+1 != arr[i]:
                return i+1
        return len(arr)+1

s = Solution()
print(s.missingNumber(arr=[3, 2, 1, 4]))