from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        positions = []
        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid[rowIndex])):
                cellValue = grid[rowIndex][colIndex]
                if cellValue == 1:
                    positions.append((rowIndex, colIndex))

        def rect_area(points):
            if len(points) == 0:
                return 0

            firstCoords = [p[0] for p in points]
            secondCoords = [p[1] for p in points]

            minRow = min(firstCoords)
            maxRow = max(firstCoords)
            minCol = min(secondCoords)
            maxCol = max(secondCoords)

            widthVal = maxRow - minRow + 1
            heightVal = maxCol - minCol + 1

            return widthVal * heightVal

        minimalSum = inf
        countPositions = len(positions)

        # Iterate over possible split sizes for comboA and comboB
        # outerIndex, middleIndex, and innerIndex are used as in pseudocode,
        # but innerIndex indexing is redundant in Python as combos are generated directly.
        # Following the logic strictly, but innerIndex does not affect combination sizes;
        # so we consider the same structure, but actually use outerIndex and middleIndex only.
        for outerIndex in range(1, countPositions):
            for middleIndex in range(outerIndex + 1, countPositions):
                sizeA = outerIndex
                sizeB = middleIndex - outerIndex
                sizeC = countPositions - middleIndex
                if sizeC <= 0:
                    continue

                # For comboA of size sizeA
                for comboA in combinations(positions, sizeA):
                    setPositions = set(positions)
                    setComboA = set(comboA)
                    remainingAfterA = setPositions - setComboA

                    # For comboB of size sizeB from remainingAfterA
                    for comboB in combinations(remainingAfterA, sizeB):
                        setComboB = set(comboB)
                        comboC = remainingAfterA - setComboB

                        areaA = rect_area(comboA)
                        areaB = rect_area(comboB)
                        areaC = rect_area(comboC)

                        if areaA > 0 and areaB > 0 and areaC > 0:
                            combinedSum = areaA + areaB + areaC
                            if combinedSum < minimalSum:
                                minimalSum = combinedSum

        return minimalSum