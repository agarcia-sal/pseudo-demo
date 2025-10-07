class Solution:
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        totalCost = 0
        idxH = 0
        idxV = 0
        heightParts = 1
        widthParts = 1
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        while idxH < len(horizontalCut) or idxV < len(verticalCut):
            if idxV == len(verticalCut) or (idxH < len(horizontalCut) and horizontalCut[idxH] > verticalCut[idxV]):
                totalCost += horizontalCut[idxH] * widthParts
                heightParts += 1
                idxH += 1
            else:
                totalCost += verticalCut[idxV] * heightParts
                widthParts += 1
                idxV += 1

        return totalCost