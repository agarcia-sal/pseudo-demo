from functools import cmp_to_key
from typing import List

class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        totalRooks = len(rooks)

        def compareFirstElement(a, b):
            if a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            else:
                return 0

        def compareSecondElement(a, b):
            if a[1] > b[1]:
                return 1
            elif a[1] < b[1]:
                return -1
            else:
                return 0

        sortedByRow = sorted(rooks, key=cmp_to_key(compareFirstElement))
        sortedByColumn = sorted(rooks, key=cmp_to_key(compareSecondElement))

        sumMovesRow = 0
        for counter in range(totalRooks):
            valOne = sortedByRow[counter][0]
            ix = counter
            delta = abs(valOne - ix)
            sumMovesRow += delta

        sumMovesCol = 0
        for counter in range(totalRooks):
            valTwo = sortedByColumn[counter][1]
            position = counter
            delta = abs(valTwo - position)
            sumMovesCol += delta

        finalSum = sumMovesRow + sumMovesCol
        return finalSum