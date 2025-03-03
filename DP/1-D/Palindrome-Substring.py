class Solution:
    def countSubstrings(self, s: str) -> int:
        res,n=0,len(s)
        def palindrome(l,r):
            count=0
            while l>=0 and r<n and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            return count

        for i in range(n):
            even=palindrome(i,i+1)
            odd=palindrome(i,i)
            res+=even+odd
        return res
