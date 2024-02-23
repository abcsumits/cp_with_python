class dsu:
    def __init__(self,n):
        self.size=[1]*(n+1)
        self.parent=[x for x in range(n+1)]
   def find(self,x):
        t=x
        while self.parent[t]!=t:
            t=self.parent[t]
        while self.parent[x]!=x:
            f=x
            x=self.parent[x]
            self.parent[f]=t
        return x
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
