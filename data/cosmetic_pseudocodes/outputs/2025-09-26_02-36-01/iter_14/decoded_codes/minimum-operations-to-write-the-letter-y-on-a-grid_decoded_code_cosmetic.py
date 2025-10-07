from typing import List, Tuple, Dict, Set

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        totalRows = len(grid)
        midPoint = totalRows // 2
        specialPositions: Set[Tuple[int, int]] = set()

        index1 = 0
        while index1 <= midPoint:
            specialPositions.add((index1, index1))
            index1 += 1

        index2 = 0
        while True:
            specialPositions.add((index2, (totalRows - index2) - 1))
            index2 += 1
            if index2 > midPoint:
                break

        for idx in range(midPoint, totalRows):
            specialPositions.add((idx, midPoint))

        def countOccurrencesAtPositions(matrix: List[List[int]], positions: Set[Tuple[int, int]]) -> Dict[int, int]:
            tally = {0: 0, 1: 0, 2: 0}
            for r, c in positions:
                val = matrix[r][c]
                tally[val] += 1
            return tally

        def countOccurrencesNotInPositions(matrix: List[List[int]], positions: Set[Tuple[int, int]]) -> Dict[int, int]:
            tally = {0: 0, 1: 0, 2: 0}
            visited = positions
            for row in range(totalRows):
                for col in range(totalRows):
                    if (row, col) not in visited:
                        val = matrix[row][col]
                        tally[val] += 1
            return tally

        countSpecialChars = countOccurrencesAtPositions(grid, specialPositions)
        countOtherChars = countOccurrencesNotInPositions(grid, specialPositions)

        minOpCount = float('inf')

        a = 0
        while a <= 2:
            b = 0
            while True:
                if a != b:
                    totalYChars = countSpecialChars[0] + countSpecialChars[1] + countSpecialChars[2]
                    totalOtherChars = countOtherChars[0] + countOtherChars[1] + countOtherChars[2]

                    opsNeeded = (totalYChars - countSpecialChars[a]) + (totalOtherChars - countOtherChars[b])

                    if opsNeeded < minOpCount:
                        minOpCount = opsNeeded
                b += 1
                if b > 2:
                    break
            a += 1

        return minOpCount