from random import getrandbits
class Wrp(int):
    RANDOM = getrandbits(32)
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrp, self).__hash__() ^ self.RANDOM 