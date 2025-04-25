
class Solution:
    def rotate(self, arr):
        n=len(arr)
        arr.reverse()
        arr[:1]=reversed(arr[:1])
        arr[1:]=reversed(arr[1:])
        return arr
    
s = Solution()
print(s.rotate(arr = [1,2,3,4,5]))