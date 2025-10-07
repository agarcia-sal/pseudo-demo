from typing import List, Set

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        max_sum = 0  # Initialize max sum as zero

        def exploreLayers(layerIndex: int, chosenSet: Set[int], aggregateValue: int) -> None:
            nonlocal max_sum
            if layerIndex >= len(grid):
                if aggregateValue > max_sum:
                    max_sum = aggregateValue
                return

            # Explore skipping current layer
            exploreLayers(layerIndex + 1, chosenSet, aggregateValue)

            # Explore picking an element from current layer if not already chosen
            for element in grid[layerIndex]:
                if element not in chosenSet:
                    chosenSet.add(element)
                    exploreLayers(layerIndex + 1, chosenSet, aggregateValue + element)
                    chosenSet.remove(element)

        # Sort each row descending order
        for i in range(len(grid)):
            grid[i].sort(reverse=True)

        exploreLayers(0, set(), 0)
        return max_sum