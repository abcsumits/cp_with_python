mod=(10**9)+7
def power(x, y, p):
    res = 1 
    x = x % p
    if (x == 0) :
        return 0
 
    while (y > 0) :
        if ((y & 1) == 1) :
            res = (res * x) % p
        y = y >> 1 
        x = (x * x) % p
    return res
def rolling_hash(imod,harray,s):
    a=1
    v=0
    for  i in range(len(s)):
        v=(v+(a*(ord(s[i])-97))%mod)%mod
        imod.append(power(a,mod-2,mod))
        a=(a*25)%mod
        harray.append(v)
def hash(x,y,harray,imod):
    if x-1<0:
        return (harray[y]*imod[0])%mod
    else:
        return (((harray[y]-harray[x-1]))*imod[x])%mod