class CommonAncestor:
    def __init__(self, n, gp,root):#gp means graph matrix, n number of nodes,root node , range of nodes is 0 to n-1 
        bit=1
        t=n
        while t:
            t//=2
            bit+=1
        bit_ancestor=[] 
        for i in range(n):
            bit_ancestor.append([-1]*bit)
        stack=[[root,0]]
        depth=[0]*n 
        while stack:
            curr=stack[-1] 
            node=curr[0]
            upcomming=curr[1] 
            if upcomming==0 and node!=root:
                c=stack[-2][0]
                for i in range(1,bit):
                    if c==-1:
                        break
                    bit_ancestor[node][i]=c 
                    c=bit_ancestor[c][i]
            if upcomming==len(gp[node]):
                stack.pop() 
            else:
                stack[-1][1]+=1
                depth[gp[node][upcomming]]=depth[node]+1
                stack.append([gp[node][upcomming],0]) 
        self.ancestor=bit_ancestor
        self.bit=bit
        self.depth=depth
        self.root=root 
 
    def getKthAncestor(self, node, k) : # returns -1 for invalid queries
        t=1
        for i in range(1,self.bit):
            if t&k:
                node=self.ancestor[node][i]
            if node==-1:
                return -1
            t<<=1
        return node
    def lca(self,x,y):
        if self.depth[x]<self.depth[y]:
            x^=y 
            y^=x 
            x^=y
        x=self.getKthAncestor(x,self.depth[x]-self.depth[y])
        max_power=self.bit-1 
        possible_anscetor=self.root
        if x==y:
            return x
        while max_power>0:
            if self.ancestor[x][max_power]!=self.ancestor[y][max_power] :
                x=self.ancestor[x][max_power]
                y=self.ancestor[y][max_power]
            max_power-=1
        return self.ancestor[x][1]
