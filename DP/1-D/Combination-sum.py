class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res=[]
        def dfs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if i>=len(nums) or total>target:
                return
            
            curr.append(nums[i])
            dfs(i,curr,total+nums[i])
            curr.pop()
            dfs(i+1,curr,total)
        dfs(0,[],0)
        return res
    
s = Solution()
print(s.combinationSum(nums = [2,3,6,7],target=7))
