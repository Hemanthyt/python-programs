class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]
        for start,end in intervals[1:]:
            last =  res[-1][1]
            if start<=last:
                res[-1][1]=max(end,res[-1][1])
            else:
                res.append([start,end])
        print(res)
        
        
    
s = Solution()
print(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))