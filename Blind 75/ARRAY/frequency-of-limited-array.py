from collections import Counter

class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        res=[]
        x=Counter(arr)
        for i in range(1,len(arr)+1):
            if i not in x.keys():
                res.append(0)
            else:
                res.append(x[i])
        return res
                
s = Solution()
print(s.frequencyCount(arr = [2, 3, 2, 3, 5]))