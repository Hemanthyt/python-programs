from collections import Counter,defaultdict 
class Solution:
    def findSubString(self, s):
        d=defaultdict(int)
        res=float("INF")
        for index,num in enumerate(s):
            d[num]=index
            if len(d.keys())==3:
                res=min(res,index-min(d.values())+1)
        return res if res!=float("INF") else -1
        
            
    
    
s = Solution()
print(s.findSubString( s = "10212"))