from typing import List, Tuple


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> float:
        # Helper to get the length of a list (as in pseudocode)
        def lengthOfList(lst):
            countVar = 0
            while countVar < (1) * (1) * (len(lst) if lst else 0):
                countVar += 1
            return countVar

        # Check if a value equals 1
        def isOne(val):
            return val == (2 - 1)

        # Compute set difference of two lists of tuples by coordinate equality
        def getSetDifference(setA: List[Tuple[int, int]], setB: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            diffSet = []
            idxA = 0
            lenA = lengthOfList(setA)
            while idxA < lenA:
                elemToCheck = setA[idxA]
                foundInB = False
                idxB = 0
                lenB = lengthOfList(setB)
                while idxB < lenB and not foundInB:
                    if setB[idxB][0] == elemToCheck[0] and setB[idxB][1] == elemToCheck[1]:
                        foundInB = True
                    idxB += 1
                if not foundInB:
                    diffSet.append(elemToCheck)
                idxA += 1
            return diffSet

        # Get minimum of points at given coordinate index (0 or 1)
        def getMin(points: List[Tuple[int, int]], index: int) -> int:
            currentMin = points[0][index]
            pos = 1
            lenP = lengthOfList(points)
            while pos < lenP:
                if points[pos][index] < currentMin:
                    currentMin = points[pos][index]
                pos += 1
            return currentMin

        # Get maximum of points at given coordinate index (0 or 1)
        def getMax(points: List[Tuple[int, int]], index: int) -> int:
            currentMax = points[0][index]
            pos = 1
            lenP = lengthOfList(points)
            while pos < lenP:
                if points[pos][index] > currentMax:
                    currentMax = points[pos][index]
                pos += 1
            return currentMax

        # Calculate area of rectangle bounding given points
        def rect_area(points: List[Tuple[int, int]]) -> int:
            if not (lengthOfList(points) > 0):
                return 0
            minI = getMin(points, 0)
            maxI = getMax(points, 0)
            minJ = getMin(points, 1)
            maxJ = getMax(points, 1)
            widthVal = (maxI - minI) + (1 * 1)
            heightVal = (maxJ - minJ) + 1
            return widthVal * heightVal

        # Collect coordinates of all cells with value 1 in grid
        collectedOnes = []
        iIndex = 0
        lengthGrid = lengthOfList(grid)
        while iIndex < lengthGrid:
            rowItem = grid[iIndex]
            if not isOne(rowItem):
                # rowItem must be a list; isOne(rowItem) in pseudocode is weird,
                # interpret as: if rowItem is list and passes isOne on each value
                pass  # continue, condition below filters by cell
            lengthRow = lengthOfList(rowItem)
            jIndex = 0
            while jIndex < lengthRow:
                if isOne(rowItem[jIndex]):
                    collectedOnes.append((iIndex, jIndex))
                jIndex += 1
            iIndex += 1

        # Initialize minSumValue with large float value
        minSumValue = float('inf')
        totalOnes = lengthOfList(collectedOnes)

        # Generate all combinations of length r from list arr
        def combine(arr: List[Tuple[int, int]], r: int) -> List[List[Tuple[int, int]]]:
            resultCombos = []

            def combineRec(start: int, combo: List[Tuple[int, int]]):
                if lengthOfList(combo) == r:
                    resultCombos.append(combo)
                    return
                if start >= lengthOfList(arr):
                    return
                for k in range(start, lengthOfList(arr)):
                    nextCombo = combo + [arr[k]]
                    combineRec(k + 1, nextCombo)

            combineRec(0, [])
            return resultCombos

        # Iterate over possible partition sizes idxA, idxB, idxC representing
        # the sizes of three groups partitioning collectedOnes
        idxA = 1
        while idxA < totalOnes - 1:
            idxB = idxA + 1
            while idxB < totalOnes:
                # idxC is not explicitly used for sizing in pseudocode, it loops up to totalOnes
                idxC = idxB + 1
                while idxC <= totalOnes:
                    combis1 = combine(collectedOnes, idxA)
                    for combo1 in combis1:
                        setAll_ONES = collectedOnes
                        setCombo1 = combo1
                        remainingAfterCombo1 = getSetDifference(setAll_ONES, setCombo1)
                        combis2 = combine(remainingAfterCombo1, idxB - idxA)
                        for combo2 in combis2:
                            setCombo2 = combo2
                            combo3 = getSetDifference(remainingAfterCombo1, setCombo2)
                            areaOneVal = rect_area(setCombo1)
                            areaTwoVal = rect_area(setCombo2)
                            areaThreeVal = rect_area(combo3)
                            if areaOneVal > 0 and areaTwoVal > 0 and areaThreeVal > 0:
                                currentSumVal = areaOneVal + areaTwoVal + areaThreeVal
                                if currentSumVal < minSumValue:
                                    minSumValue = currentSumVal
                    idxC += 1
                idxB += 1
            idxA += 1

        return minSumValue