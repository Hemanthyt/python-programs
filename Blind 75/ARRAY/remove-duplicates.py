class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        a=list(set(arr))
        a.sort()
        for i in range(len(a)):
            arr[i]=a[i]
        print(a)
        print(arr)
        # return len(a)
s = Solution()
print(s.removeDuplicates(arr = [2, 2, 2, 2, 2] ))
print(s.removeDuplicates(arr = [1, 2, 3, 2, 2] ))