def f(a,x,y):
    while x<y:
        t=a[x]
        a[x]=a[y]
        a[y]=t
        y-=1
        x+=1