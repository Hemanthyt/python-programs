class Solution(object):
    def hasMatch(self, s, p):
        l,r=0,0
        while l<len(s) and r<len(p):
            print(s[l],p[r])
            if s[l] == s[r]:
                l+=1
                r+=1
            elif p[r]=="*":
                r+=1
            else:
                l+=1
        return l==len(s) and r==len(p)
            

s = Solution()
# print(s.hasMatch( "car", p = "c*v"))
print(s.hasMatch( s = "leetcode", p = "ee*e"))