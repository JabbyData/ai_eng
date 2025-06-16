class Solution:

    def __init__(self, w: List[int]):
        self.vals = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        return bisect.bisect(self.vals,random.randint(0,self.vals[-1]-1))