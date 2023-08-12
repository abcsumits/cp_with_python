#remember file names are input.txt and output.txt 
#remember to pass only one argument to print
#add this lines before your program and after defining fast io(or that will over write testing)
#after testing done set flag =0
flag=1
if flag:
    class out:
        def __init__(self):
            self.fo=open("output.txt","w")
        def inu(self,x):
            if str(type(x))!="<class 'str'>":
                x=str(x)
            self.fo.write(x)
            self.fo.write("\n")
    class inp:
        def __init__(self):
            self.fi=open("input.txt","r")
        def inu(self):
            return self.fi.readline()[:-1]
    fy=out()
    print=fy.inu
    fx=inp()
    input=fx.inu
