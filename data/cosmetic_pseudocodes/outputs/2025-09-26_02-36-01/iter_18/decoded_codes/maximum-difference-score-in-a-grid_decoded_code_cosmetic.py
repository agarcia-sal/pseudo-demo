from math import inf
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        a = len(grid)
        b = len(grid[0])
        matrix = [[inf] * b for _ in range(a)]
        matrix[0][0] = grid[0][0]
        result = -inf

        for idx in range(1, b):
            matrix[0][idx] = min(matrix[0][idx - 1], grid[0][idx])

        for row in range(1, a):
            matrix[row][0] = min(matrix[row - 1][0], grid[row][0])

        for outer in range(1, a):
            for inner in range(1, b):
                matrix[outer][inner] = min(matrix[outer][inner - 1], matrix[outer - 1][inner])
                val = grid[outer][inner] - matrix[outer][inner]
                if val > result:
                    result = val

        return result