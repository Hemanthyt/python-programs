class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr):
        #code here
        # arr.sort()
        # for i in range(len(arr)):
        #     a=arr[i]
        #     l=i+1
        #     r=len(arr)-1
        #     while l<r:
        #         s = a+arr[l]+arr[r]
        #         if s==0:
        #             return True
        #         elif s<0:
        #             l+=1
        #         else:
        #             r-=1
        # return False
        
        arr.sort()
        res=[]
        if len(arr)<3:
            return []
            
        for i in range(0,len(arr)-2):
            if i>0 and arr[i]==arr[i-1]:
                continue
            a=arr[i]
            l=i+1
            r=len(arr)-1
            while l<r:
                s=a+arr[l]+arr[r]
                if s==0:
                    res.append([a,arr[l],arr[r]])
                    l+=1
                    r-=1
                    while arr[l]==arr[l-1] and l<r:
                        l+=1
                    while arr[r]==arr[r+1] and l<r:
                        r-=1
                elif s<0:
                    l+=1
                    while arr[l]==arr[l-1] and l<r:
                        l+=1
                elif s>0:
                    r-=1
                    while arr[r]==arr[r+1] and l<r:
                        r-=1
        return res
                    
    
                    

s = Solution()
# print(s.findTriplets(arr = [0, 1, 2, 3, 1] ))
print(s.findTriplets(arr =[-1,0,1,2,-1,-4]))