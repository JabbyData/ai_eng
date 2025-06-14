"""
Problem : Given array of int nums, return if there exists a subarray of size >= 2 whose sum % k = 0
Idea : (a+b)%k = (a%k + b%k)%k and x%k in [0,...,k-1]. 
Compute cumulative sum and apply modulo every time, if remainder already seen at least 2 steps ago then a multiple of k has been computed by summing within.
Complexity : O(n)
"""
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = {0: -1}
        r = 0
        for i in range(len(nums)):
            r += nums[i]
            r %= k
            if r in cache.keys():
                if i >= cache[r] + 2:
                    return True
            else:
                cache[r] = i
        return False