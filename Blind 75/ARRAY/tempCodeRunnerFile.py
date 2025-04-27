
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True