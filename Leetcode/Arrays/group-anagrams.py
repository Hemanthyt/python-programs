from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d={}
        for i in strs:
            s="".join(sorted(i))
            if s not in d:
                d[s] = [i]
            else:
                d[s].append(i)
        return d.values()
                
s = Solution()
print(s.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))