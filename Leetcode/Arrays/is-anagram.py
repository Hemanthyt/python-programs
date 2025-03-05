class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        return s==t
        
        
s = Solution()
print(s.isAnagram( s = "racecar", t = "carrace"))