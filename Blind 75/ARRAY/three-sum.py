class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        # arr.sort()
        # print(arr)
        # for i in range(len(arr)):
        #     a=arr[i]
        #     l, r = i + 1, len(arr) - 1
        #     while l<r:
        #         s=a+arr[l]+arr[r]
        #         if s == target:
        #             return True
        #         elif s < target:
        #             l += 1
        #         else:
        #             r -= 1
        # return False
        
        arr.sort()
        res=[]
        
                
        
s = Solution()
print(s.hasTripletSum(arr = [1, 4, 45, 6, 10, 8], target = 14 ))
