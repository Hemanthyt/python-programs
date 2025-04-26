class Solution:
    def sort012(self, arr):
        c0 = arr.count(0)
        c1 = arr.count(1)
        c2 = arr.count(2)
        
        for i in range(len(arr)):
            if i<c0:
                arr[i]=0
            elif i>=c0 and i<(c0+c1):
                arr[i]=1
            else:
                arr[i] = 2
        return arr

s = Solution()
print(s.sort012(arr=[1,0 ,2 ,1, 1, 1, 0]))