from collections import Counter,defaultdict 
class Solution:
    def findSubString(self, s):
        # Your code goes here
        n=len(s)
        window_size=len(Counter(s))
        d=defaultdict(int)
        l=0
        min_size=n
        for r in range(n):
            d[s[r]]+=1
            while len(d)==window_size:
                print(r-l+1)
                min_size=min(min_size,r-l+1)
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
        return min_size
            
            
s = Solution()
print(s.findSubString( s = "GEEKSGEEKSFOR"))