from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        x1 = len(grid)
        x2 = len(grid[0])
        count = 0

        index_j = 0
        while index_j <= x2 - 1:
            index_i = 0
            while index_i <= x1 - 2:
                if grid[index_i][index_j] != grid[index_i + 1][index_j]:
                    count += 1
                    grid[index_i + 1][index_j] = grid[index_i][index_j]
                index_i += 1

            index_k = 0
            while index_k <= x1 - 1:
                if index_j < x2 - 1 and grid[index_k][index_j] == grid[index_k][index_j + 1]:
                    count += 1
                    candidate_value = 0
                    while candidate_value <= 9:
                        if candidate_value != grid[index_k][index_j]:
                            grid[index_k][index_j + 1] = candidate_value
                            break
                        candidate_value += 1
                index_k += 1

            index_j += 1

        return count