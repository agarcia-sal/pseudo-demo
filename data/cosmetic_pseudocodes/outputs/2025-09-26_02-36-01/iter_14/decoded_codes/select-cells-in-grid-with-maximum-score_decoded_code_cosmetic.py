from typing import List, Set

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # Sort each sublist in descending order (bubble sort as per pseudocode)
        for sublist in grid:
            i = 0
            while i < len(sublist) - 1:
                j = i + 1
                while j < len(sublist):
                    if sublist[j] > sublist[i]:
                        sublist[i], sublist[j] = sublist[j], sublist[i]
                    j += 1
                i += 1

        maxValue = 0

        def recurse(currentIndex: int, takenSet: Set[int], aggregate: int) -> None:
            nonlocal maxValue
            if currentIndex >= len(grid):
                if aggregate > maxValue:
                    maxValue = aggregate
                return

            # Case: skip current row
            recurse(currentIndex + 1, takenSet, aggregate)

            # Try including elements in current row if not taken
            for element in grid[currentIndex]:
                if element not in takenSet:
                    takenSet.add(element)
                    recurse(currentIndex + 1, takenSet, aggregate + element)
                    takenSet.remove(element)

        recurse(0, set(), 0)
        return maxValue