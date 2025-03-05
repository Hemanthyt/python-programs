class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res=nums1+nums2
        res.sort()
        print(res)
        if len(res)%2==0:
            return (res[len(res)//2-1]+res[len(res)//2])/2
        else:
            return res[len(res)//2]
s = Solution()
print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3]))