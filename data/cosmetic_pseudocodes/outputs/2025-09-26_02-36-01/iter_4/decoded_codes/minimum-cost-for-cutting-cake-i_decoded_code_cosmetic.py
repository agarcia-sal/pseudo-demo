class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        descendingHorizontalCuts = sorted(horizontalCut, reverse=True)
        descendingVerticalCuts = sorted(verticalCut, reverse=True)

        totalCost = 0
        horizontalIndex = 0
        verticalIndex = 0
        horizontalSegments = 1
        verticalSegments = 1

        while not (horizontalIndex >= m - 1 and verticalIndex >= n - 1):
            if verticalIndex == n - 1 or (horizontalIndex < m - 1 and descendingHorizontalCuts[horizontalIndex] > descendingVerticalCuts[verticalIndex]):
                increment = descendingHorizontalCuts[horizontalIndex]
                weightedIncrement = increment * verticalSegments
                totalCost += weightedIncrement
                horizontalSegments += 1
                horizontalIndex += 1
            else:
                increment = descendingVerticalCuts[verticalIndex]
                weightedIncrement = increment * horizontalSegments
                totalCost += weightedIncrement
                verticalSegments += 1
                verticalIndex += 1

        return totalCost