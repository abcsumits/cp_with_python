#p[2*i+1]-1 represents maximum length of odd center palindorme with center i 
#p[2*i+2]-1 represents maximum length of even center palindorme with center at i and i+1
#dont forget mistake of fast i/o ends with \n
def p_arr(s):
    temp=["#"]
    for x in s:
        temp.append(x)
        temp.append("#")
    l=0
    r=0
    p=[1]*len(temp)
    for i in range(len(temp)):
        t=min(p[r+l-i],r-i+1)
        while i+t<len(temp) and i-t>=0:
            if temp[i+t]==temp[i-t]:
                t+=1
            else:
                break 
        p[i]=t
        if i+t-1>r:
            r=i+t-1
            l=i-t+1
    return p        