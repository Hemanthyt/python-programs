class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        final=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            final[i]=pre
            pre*=nums[i]
        
        suf=1
        for i in range(len(nums)-1,-1,-1):
            final[i]*=suf
            suf*=nums[i]
            
        print(final)
    
s = Solution()
print(s.productExceptSelf(nums = [1,2,4,6]))
        