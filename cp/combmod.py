mod=10**9+7
def power(x, y, mod):
    res = 1 
    x = x % mod
    if (x == 0) :
        return 0
 
    while (y > 0) :
        if ((y & 1) == 1) :
            res = (res * x) % mod
        y = y >> 1 
        x = (x * x) % mod
    return res
def inverse_modulo(x,mod):
    #fermat little theorem only valid for prime ,else use euler totient function
    return power(x,mod-2,mod)
def nCr(n,r,mod):
    if n<r:
        return 0
    if r==0:
        return 1
    numerator=1
    denominator=1
    for i in range(1,r+1):
        numerator*=(n-r+i)
        numerator%=mod
        denominator*=i
        denominator%=mod 
    return (numerator*(inverse_modulo(denominator,mod)))%mod 

    
    
