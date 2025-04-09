class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        res=0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
                    res+=1
        return res


s = Solution()
print(s.inversionCount( arr = [2, 4, 1, 3, 5]))
print(s.inversionCount( arr = [57 ,38, 91, 10 ,38, 28, 79, 41]))