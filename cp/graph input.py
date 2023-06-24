n,e=map(int,input().split())
gp=[]
for i in range(n):
    gp.append([])
for i in range(e):
    x,y=map(int,input().split())
    gp[x-1].append(y-1)
    gp[y-1].append(x-1)