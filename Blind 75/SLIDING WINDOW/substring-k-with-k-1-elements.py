class Solution:
    def countOfSubstrings(self, s, K):
        # code here 
        d={}
        i=0
        j=0
        count=0
        n=len(s)
        while j<n:
            if s[j] not in d:
                d[s[j]]=1
            else:
                d[s[j]]+=1
            if j-i+1==K:
                if len(d) == K-1:
                    count+=1
                d[s[i]]-=1
                if d[s[i]]==0:
                    del d[s[i]]
                i+=1
            j+=1
        return count
        
s = Solution()
print(s.countOfSubstrings(s = "abcc", K = 2))