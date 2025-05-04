from collections import Counter,defaultdict 

class Solution:
    
    #Function to find the smallest window in the string s1 consisting
    #of all the characters of string s2.
    def smallestWindow(self, s1, s2):
        #code here
        n1=len(s1)
        window_size=len(Counter(s2))
        min_size = n1
        d=defaultdict(int)
        
        for r in range(n1):
            d[s[r]]+=1
            if len(d)==window_size:
                
            



s = Solution()
print(s.smallestWindow(  s1 = "timetopractice", s2 = "toc"))