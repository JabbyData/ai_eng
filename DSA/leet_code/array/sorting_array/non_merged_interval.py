
"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        answer = 0
        end = None
        for interval in intervals:
            if end is None:
                end = interval[1]
                continue
            if interval[0] < end:
                answer += 1
                end = min(end,interval[1])
            else:
                end = interval[1]
        return answer
        