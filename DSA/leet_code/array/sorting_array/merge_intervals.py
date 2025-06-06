"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        answer=[interval[0]]
        for interval in intervals:
            if answer[-1][1]<interval[0]:
                answer.append(interval)
            else:
                answer[-1][1]=max(answer[-1][1],interval[1])
        return answer