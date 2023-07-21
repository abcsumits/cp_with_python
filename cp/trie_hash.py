class Trie:
    def __init__(self):
        self.d={}
        self.chk=False
    def insert(self, word: str) -> None:
        t=self
        for x in word:
            if x in t.d:
                t=t.d[x]
            else:
                t.d[x]=Trie()
                t=t.d[x]
        t.chk=True
    def search(self, word: str) -> bool:
        t=self
        for x in word:
            if x in t.d:
                t=t.d[x]
            else:
                return False
        if t.chk:
            return True
        return False
    def startsWith(self, prefix: str) -> bool:
        t=self
        for x in prefix:
            if x in t.d:
                t=t.d[x]
            else:
                return False
        return True
        
