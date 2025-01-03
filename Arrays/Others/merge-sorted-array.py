class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()
        # for i in nums2:
        #     nums1.append(i)
        return nums1
        

s = Solution()
print(s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))