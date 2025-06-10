"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Idea : 
- Precompute in linear time all suffixe product, reverse the order and iterate while incrementing a prefix product
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        suf_mult = [0] * (n-1)
        p_suf = 1
        for i in range(1,n):
            p_suf *= nums[n-i]
            suf_mult[n-1-i] = p_suf
        answer = [0] * n
        prefix = 1
        for i in range(n-1):
            answer[i] = prefix * suf_mult[i]
            prefix *= nums[i]
        answer[n-1] = prefix
        return answer