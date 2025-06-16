"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

    a 1-day pass is sold for costs[0] dollars,
    a 7-day pass is sold for costs[1] dollars, and
    a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

    For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Idea : dp array storing minimum cost until idx associated + checked if day need to be updated
"""


from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1]
        cum_arr = [0] * (max_day+1)
        days = set(days)
        for day in range(max_day+1):
            if not day in days:
                cum_arr[day] = cum_arr[day-1]
            else:
                cum_arr[day] = min(cum_arr[max(0,day-1)]+costs[0],cum_arr[max(0,day-7)]+costs[1],cum_arr[max(0,day-30)]+costs[2])
        return cum_arr[-1]