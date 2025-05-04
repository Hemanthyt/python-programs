class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={")":"(","]":"[","}":"{"}
        for i in s:
            if i in d.values():
                st.append(i)
            elif i in d.keys():
                if not st or d[i]!=st.pop():
                    return False
        return not st
        
        
        
s = Solution()
print(s.isValid( s = "()[]{}"))