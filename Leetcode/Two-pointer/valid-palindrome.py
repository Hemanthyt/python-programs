import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub('[^a-zA-Z0-9]',"",s).lower()
        print(s)
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True
s = Solution()
print(s.isPalindrome( s = "Was it a car or a cat I saw?"))