"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = end = 0
        curr_sum = 0
        min_len = float("inf")
        
        while end < n:
            curr_sum += nums[end]

            while curr_sum >= target:
                min_len = min(min_len,end-start+1)
                curr_sum -= nums[start]
                start += 1
            
            end += 1
        
        if min_len == float("inf"):
            return 0
        else:
            return min_len
