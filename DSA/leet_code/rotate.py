from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left,right):
            while right > left:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1

        if k != 0:
            n = len(nums)
            k = k % n
            reverse(0,n-1)
            reverse(0,k-1)
            reverse(k,n-1)
