class Solution:
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        ##Your code here
        #Return true or false
        sett=set()
        cs=0
        for num in arr:
            cs+=num
            if cs==0 or cs in sett:
                return True
            sett.add(cs)
            print(sett)
        return False
            

s = Solution()
print(s.subArrayExists(arr= [4, 2, -3, 1, 6]))