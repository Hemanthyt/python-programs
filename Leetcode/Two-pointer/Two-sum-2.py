class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        d={}
        for i in range(len(numbers)):
            if numbers[i] in d:
                return [d[numbers[i]]+1,i+1]
            else:
                d[target - numbers[i]]=i
        return False
    

            
s = Solution()
# print(s.twoSum( numbers = [1,2,3,4], target = 3))
print(s.twoSum( numbers=[2,3,4],target=6))