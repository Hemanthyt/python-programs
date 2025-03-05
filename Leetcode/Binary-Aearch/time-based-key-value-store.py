class TimeMap:

    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[]
        self.d[key].append([value,timestamp])
        print( self.d)
        
    def get(self, key: str, timestamp: int) -> str:
        res,values="",self.d.get(key,[])
        l,r=0,len(values)-1
        while l<=r:
            m=(l+r)//2
            if values[m][1]<=timestamp:
                res=values[m][0]
                l=m+1
            else:
                r=m-1
        print( self.d)
        print(res)
        
                
timeMap = TimeMap();
timeMap.set("alice", "happy", 1);  
# timeMap.get("alice", 1);
# timeMap.get("alice", 2);           
timeMap.set("alice", "beep", 2);    
timeMap.set("alice", "sad", 3);    
timeMap.set("alice", "no", 4);    
timeMap.get("alice", 3);         