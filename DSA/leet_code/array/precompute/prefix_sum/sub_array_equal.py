"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k

Idea : cum sum + sum freq in hash table, if sum already seen then add freq to res (cf can combine with all freq other subarrays)
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        curr_s = 0
        res = 0
        for i in range(len(nums)):
            curr_s += nums[i]
            if curr_s - k in freq:
                res += freq[curr_s-k]
            if curr_s not in freq:
                freq[curr_s] = 1
            else:
                freq[curr_s] += 1
        return res