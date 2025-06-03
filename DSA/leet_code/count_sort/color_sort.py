"""
Given an array nums with n objects colored red (0), white (1), or blue (2), sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        # Counting
        for elt in nums:
            counts[elt] += 1
        # Sort (overwrite)
        for i in range(counts[0]):
            nums[i] = 0
        for i in range(counts[0], counts[0] + counts[1]):
            nums[i] = 1
        for i in range(counts[0] + counts[1], counts[0] + counts[1] + counts[2]):
            nums[i] = 2