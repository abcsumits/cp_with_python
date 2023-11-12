class segmenttree:

    def __init__(self, nums: List[int]):
        n=len(nums)
        c=0
        t=0
        while n>1:
            if n%2>0:
                c=1
            t+=1
            n=n//2
        t+=c
        n=2**t
        self.segmenttree=[0]*(2*n-1)
        for i in range(len(nums)):
            self.segmenttree[n-1+i]=nums[i]
        for i in range(n-2,-1,-1):
            self.segmenttree[i]=self.segmenttree[2*i+1]+self.segmenttree[2*i+2]
        self.n=n
    def update(self, index: int, val: int) -> None:
        t=index+self.n-1
        self.segmenttree[t]=val
        t=(t-1)//2
        while t>=0:
            self.segmenttree[t]=self.segmenttree[t*2+1]+self.segmenttree[2*t+2]
            t=(t-1)//2

    def sumRange(self, left: int, right: int) -> int:
        left=left+self.n-1
        right=right+self.n-1
        if left==right:
            return self.segmenttree[left]
        ans=self.segmenttree[left]
        ans+=self.segmenttree[right]
        pl=left
        pr=right
        left=(left-1)//2
        right=(right-1)//2
        while left<right:
            if pl!=left*2+2:
                ans+=self.segmenttree[left*2+2]
            if pr!=right*2+1:
                ans+=self.segmenttree[right*2+1]
            pl=left
            pr=right
            left=(left-1)//2
            right=(right-1)//2
        return ans
