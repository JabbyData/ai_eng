"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Idea : left-right appraoch, dp array storing at each index the minimum number of squared nbs used to sum to idx
"""


import sys

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [x**2 for x in list(range(1,int(n**0.5)+1))]
        sum_squares = [0] + [sys.maxsize] * n
        for i in range(n):
            for square in squares:
                new_index = i + square
                if new_index <= n:
                    sum_squares[new_index] = min(sum_squares[i]+1,sum_squares[new_index])
        return sum_squares[-1]