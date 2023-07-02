spf=[0]*(n-1)#0 index refer to 2  so on
for i in range(2,n+1):
    if spf[i-2]==0:
        spf[i-2]=i
        c=i+i
    while c<=n:
        if spf[c-2]==0:
            spf[c-2]=i
        c+=i