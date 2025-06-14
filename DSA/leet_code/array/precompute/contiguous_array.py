"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Idea : cum sum counter balancing 0 and 1 + index tracking first occ of sum in hashmap
"""
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = {0:-1}
        max_len = 0
        s = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                s -= 1
            else:
                s += 1
            if s not in sums:
                sums[s] = i
            else:
                max_len = max(max_len,i-sums[s])
        return max_len