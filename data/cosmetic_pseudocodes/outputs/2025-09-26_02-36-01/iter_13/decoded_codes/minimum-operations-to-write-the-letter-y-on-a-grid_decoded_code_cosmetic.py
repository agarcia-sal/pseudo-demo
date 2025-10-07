from math import inf
from typing import List, Tuple, Set

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        totalLength = len(grid)
        midPoint = (totalLength - (totalLength % 2)) // 2
        positionSet: Set[Tuple[int, int]] = set()

        def collectDiagonalIndices(index: int, limit: int, step: int, collector: Set[Tuple[int, int]], isPrimary: bool) -> None:
            if step > 0:
                if index > limit:
                    return
            else:
                if index < limit:
                    return
            if isPrimary:
                collector.add((index, index))
            else:
                collector.add((index, totalLength - index - 1))
            collectDiagonalIndices(index + step, limit, step, collector, isPrimary)

        collectDiagonalIndices(0, midPoint, 1, positionSet, True)
        collectDiagonalIndices(0, midPoint, 1, positionSet, False)

        row = midPoint
        while row <= totalLength - 1:
            positionSet.add((row, midPoint))
            row += 1

        def countValuesAtPositions(matrix: List[List[int]], positions: List[Tuple[int, int]]) -> List[int]:
            counts = [0, 0, 0]
            for r, c in positions:
                counts[matrix[r][c]] += 1
            return counts

        def countValuesOutsidePositions(matrix: List[List[int]], positions: Set[Tuple[int, int]]) -> List[int]:
            counts = [0, 0, 0]
            allPoints = {(r, c) for r in range(totalLength) for c in range(totalLength)}
            excludedPoints = allPoints - positions
            pointsList = list(excludedPoints)
            idx2 = len(pointsList) - 1
            while idx2 >= 0:
                rr, cc = pointsList[idx2]
                counts[matrix[rr][cc]] += 1
                idx2 -= 1
            return counts

        yPositionsCount = countValuesAtPositions(grid, list(positionSet))
        otherPositionsCount = countValuesOutsidePositions(grid, positionSet)

        minOps = inf

        candidateY = 0
        while True:
            if candidateY > 2:
                break
            candidateNonY = 0
            while True:
                if candidateNonY > 2:
                    break
                if candidateY != candidateNonY:
                    sumY = sum(yPositionsCount)
                    sumNonY = sum(otherPositionsCount)
                    opsNeeded = (sumY - yPositionsCount[candidateY]) + (sumNonY - otherPositionsCount[candidateNonY])
                    if opsNeeded < minOps:
                        minOps = opsNeeded
                candidateNonY += 1
            candidateY += 1

        return minOps