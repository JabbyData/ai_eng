"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
Idea : iterate from right to left and use a queue to store hotter days compared to the current observed temp.
"""

from collections import deque

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        queue = deque()
        n = len(temperatures)
        res = [0] * n

        for i in range(n-1,-1,-1):
            if not queue:
                queue.appendleft(i)
            
            else:
                while queue and temperatures[i] >= temperatures[queue[0]]:
                    queue.popleft()
                
                if queue:
                    res[i] = queue[0] - i
            queue.appendleft(i)
        
        return res