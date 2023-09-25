spf=[0]*(n+1)
for i in range(2,n+1):
    if spf[i]==0:
        spf[i]=i
        c=i+i
        while c<=n:
            if spf[c]==0:
                spf[c]=i
            c+=i

