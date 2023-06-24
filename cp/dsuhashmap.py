class dsu:
    def __init__(self):
        self.size={}
        self.parent={}
    def find(self,x):
        if x==self.parent[x]:
            return x
        self.parent[x]=dsu.find(self,self.parent[x])
        return self.parent[x]
    def union(self,u,v):
        if u not in self.parent:
            self.parent[u]=u
            self.size[u]=1
        x=dsu.find(self,u)
        if v not in self.parent:
            self.size[v]=1
            self.parent[v]=v
        y=dsu.find(self,v)
        if x==y:
            return
        if self.size[x]>self.size[y]:
            self.size[x]+=self.size[y]
            self.parent[y]=x
        else:
            self.size[y]+=self.size[x]
            self.parent[x]=y