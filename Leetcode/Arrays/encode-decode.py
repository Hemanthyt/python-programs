class Solution:
    
    def encode(self, strs: list[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"#"+i
        return res
    def decode(self, s: str) -> list[str]:
        4#neet4#code4#love3#you
        res,i=[],0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
s = Solution()
print(s.encode(strs=  ["neet","code","love","you"]))
print(s.decode( s = "4#neet4#code4#love3#you"))


