class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return  True
            if nums[l]<=nums[m]:
                if target < nums[l] or target > nums[m]:
                    l=m+1
                else:
                    r=m-1  
                    # 3,4,5,6,1,2
            else:
                if target < nums[m] or target > nums[r]:
                    r=m-1  
                else:
                    l=m+1
        return False
        
        
s = Solution()
print(s.search(nums = [3,4,5,6,1,2], target = 4))
