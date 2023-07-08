# no. of factors of x between [a,b] both included
def f(a,b,x):
    if a%x==0:
        return ((b-(b%x))//x)-((a)//x)+1
    return ((b-(b%x))//x)-((a+x-(a%x))//x)+1
