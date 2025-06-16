"""
Given a 2D matrix matrix, handle multiple queries of the following type:

    Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

    NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

You must design an algorithm where sumRegion works on O(1) time complexity.
"""

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n_rows, n_cols = len(matrix), len(matrix[0])
        self.grid = [[0] * (n_cols+1) for _ in range(n_rows+1)]

        for i in range(1,n_rows+1):
            for j in range(1,n_cols+1):
                self.grid[i][j] = matrix[i-1][j-1] + self.grid[i-1][j] + self.grid[i][j-1] - self.grid[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.grid[row2+1][col2+1] - self.grid[row1][col2+1] - self.grid[row2+1][col1] + self.grid[row1][col1]