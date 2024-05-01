class TreeAncestor:

    def __init__(self, n, gp,root):#gp means graph matrix, n number of nodes,root node ,nodes ranges from 0 to n-1 
        bit=1
        t=n
        while t:
            t>>=2
            bit+=1
        bit_ancestor=[] 
        for i in range(n):
            bit_ancestor.append([-1]*bit)
        stack=[[root,0]] 
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
                stack.append([gp[node][upcomming],0]) 
        self.ancestor=bit_ancestor
        self.bit=bit



        

    def getKthAncestor(self, node, k) : # returns -1 for invalid queries
        t=1
        for i in range(1,self.bit):
            if t&k:
                node=self.ancestor[node][i]
            if node==-1:
                return -1
            t<<=1
        return node
