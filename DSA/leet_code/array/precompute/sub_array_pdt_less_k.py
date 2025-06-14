"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Idea : prefix sum 
"""

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = end = 0
        pdt = 1
        res = 0
        while end < len(nums):
            pdt *= nums[end]
            while start <= end and pdt >= k:
                pdt = pdt // nums[start]
                start += 1
            res += end - start + 1
            end += 1
        return res