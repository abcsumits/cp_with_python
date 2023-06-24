# use python3 ,pypy3 will give memory limit exceed
import threading
import sys
sys.setrecursionlimit(10**8)
def main():
    #code
    pass
threading.stack_size(10 ** 8)#2*10**5->2*10**8 and so on  change it linear .
t = threading.Thread(target=main)
t.start()
t.join()
