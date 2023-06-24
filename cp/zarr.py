def zarr(z,a):
    l=0
    r=0
    n=len(a)
    c=0
    for i in range(1,n):
        if  i<r:
            if z[i-l]+i<r:
                z.append(z[i-l])
            else:
                y=r
                while y<n:
                    if a[y-i]==a[y]:
                        y+=1
                    else:
                        break
                z.append(y-i)
                r=y
                l=i
        else:
            c=0
            while i+c<n:
                if a[i+c]==a[c]:
                    c+=1
                else:
                    break
            l=i
            r=i+c
            z.append(c)