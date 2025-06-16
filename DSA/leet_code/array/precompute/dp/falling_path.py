"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Idea : cumulative top left bottom right approach.
"""


from typing import List
import sys

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        for i in range(1,n):
            for j in range(n):
                if j == 0:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i-1][j+1]) + matrix[i][j]
                elif j == n-1:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i-1][j-1]) + matrix[i][j]
                else:
                    matrix[i][j] = min(matrix[i-1][j+1],matrix[i-1][j],matrix[i-1][j-1]) + matrix[i][j]
        res = sys.maxsize
        for elt in matrix[n-1]:
            res = min(res,elt)
        return res