from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        total_cost = 0
        count_h = 1
        count_v = 1
        index_h = 0
        index_v = 0

        # Sort descending using built-in sort for efficiency
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        while not (index_h >= m - 1 and index_v >= n - 1):
            if index_v == n - 1 or (index_h < m - 1 and horizontalCut[index_h] > verticalCut[index_v]):
                total_cost += horizontalCut[index_h] * count_v
                count_h += 1
                index_h += 1
            else:
                total_cost += verticalCut[index_v] * count_h
                count_v += 1
                index_v += 1

        return total_cost