# use python3 ,pypy3 will give memory limit exceed
import threading
import sys
sys.setrecursionlimit(10**8)
def main():
    #code
    pass
threading.stack_size(10 ** 8)
t = threading.Thread(target=main)
t.start()
t.join()