s="aaabbaa"
cnt=0
for i in range(len(s)-1):
    # print(s[i]!="a")
    if (s[i]!="a") and (s[i]!="b"):
        print("A ila "+s[i])
    if s[i]=="a" and s[i+1]=="b":
        cnt+=1
    else:
        cnt+=1
print(cnt)
print(cnt<=1)
    