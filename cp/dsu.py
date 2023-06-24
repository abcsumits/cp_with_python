class dsu:
    def __init__(self,n):
        self.size=[1]*(n+1)
        self.parent=[x for x in range(n+1)]
    def find(self,x):
        if x==self.parent[x]:
            return x
        self.parent[x]=dsu.find(self,self.parent[x])
        return self.parent[x]
    def union(self,u,v):
        x=dsu.find(self,u)
        y=dsu.find(self,v)
        if x==y:
            return
        elif self.size[x]>self.size[y]:
            self.size[x]+=self.size[y]
            self.parent[y]=x
        else:
            self.size[y]+=self.size[x]
            self.parent[x]=y