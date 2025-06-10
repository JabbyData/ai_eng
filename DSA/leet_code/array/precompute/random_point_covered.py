"""
Problem : given a list of non-overlapping arrays, select a random covered point
Every point should have the same chance of being chosen

Idea : 
- Accumulate the number of covered point (starting from 0) and choose a random point index <= nb_total_covered
"""

import random
import itertools
from typing import List
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        for rect in rects:
            self.weights.append((rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1))
        self.total = sum(self.weights)
        self.weights = [0] + list(itertools.accumulate(self.weights))

    def pick(self) -> List[int]:
        index = bisect.bisect_left(self.weights, random.randint(1, self.total))
        rect = self.rects[index-1]
        return [random.randint(rect[0],rect[2]), random.randint(rect[1],rect[3])]