class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        sortedHoriz = sorted(horizontalCut, reverse=True)
        sortedVert = sorted(verticalCut, reverse=True)

        totalCost = 0
        horizIndex = 0
        vertIndex = 0
        horizSegments = 1
        vertSegments = 1

        while horizIndex < len(sortedHoriz) or vertIndex < len(sortedVert):
            if vertIndex == len(sortedVert) or (horizIndex < len(sortedHoriz) and sortedHoriz[horizIndex] > sortedVert[vertIndex]):
                totalCost += sortedHoriz[horizIndex] * vertSegments
                horizSegments += 1
                horizIndex += 1
            else:
                totalCost += sortedVert[vertIndex] * horizSegments
                vertSegments += 1
                vertIndex += 1

        return totalCost