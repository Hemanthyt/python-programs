
class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
    
s = Solution()
print(s.search(arr=[3, 2, 1, 56, 10000, 167],x=56))