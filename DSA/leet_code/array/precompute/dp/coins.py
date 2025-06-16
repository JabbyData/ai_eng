
from typing import List
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        cost = [0] + [amount+1] * amount
        visit = deque()
        visit.append(0) # always contain legit indexes
        while visit:
            idx = visit.popleft()
            for coin in coins:
                if idx + coin == amount:
                    return 1 + cost[idx]
                elif idx + coin < amount and (1 + cost[idx] < cost[idx+coin]):
                    cost[idx+coin] = 1 + cost[idx]
                    visit.append(idx+coin)
        return -1
        