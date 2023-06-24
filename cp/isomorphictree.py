def treehashisomorphic(t,a,d,x):
    a.sort()
    r=str(a)
    if r in t:
        d[x]=t[r]
    else:
        d[x]=len(t)
        t[r]=d[x]
def dfs(x,v,gp,d,t):
    v[x]=1
    a=[]
    for i in range(len(gp[x])):
        if v[gp[x][i]]==0:
            a.append(dfs(gp[x][i],v,gp,d,t))
    treehashisomorphic(t,a,d,x)
    return d[x]