class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        sumAccum = 0
        idxA = 0
        idxB = 0
        countHeight = 1
        countWidth = 1

        horizDesc = sorted(horizontalCut, reverse=True)
        vertDesc = sorted(verticalCut, reverse=True)

        len_horiz = len(horizDesc)
        len_vert = len(vertDesc)

        while True:
            if not (idxA < len_horiz or idxB < len_vert):
                break
            condLeft = (idxB == len_vert)
            condRight = (idxA < len_horiz and horizDesc[idxA] > vertDesc[idxB] if idxB < len_vert else True)
            if condLeft or condRight:
                sumAccum += horizDesc[idxA] * countWidth
                countHeight += 1
                idxA += 1
            else:
                sumAccum += vertDesc[idxB] * countHeight
                countWidth += 1
                idxB += 1

        return sumAccum