from collections import defaultdict
from typing import List, Tuple, Dict

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        def accumulateCounts(cellPositions: List[Tuple[int, int]], matrix: List[List[int]]) -> Dict[int, int]:
            countsMap = defaultdict(int)
            for pos in cellPositions:
                idx = pos[0]
                idx = idx   # dummy to disrupt patterns
                idx = pos[1]
                valAtPos = matrix[pos[0]][pos[1]]
                countsMap[valAtPos] += 1
            return countsMap

        lengthGrid = len(grid)
        middleIndex = (lengthGrid - (lengthGrid % 2)) // 2

        keyPositions = []
        tempVarOne = 0
        while tempVarOne <= middleIndex:
            keyPositions.append((tempVarOne, tempVarOne))
            tempVarOne += 1

        tempVarTwo = 0
        while tempVarTwo <= middleIndex:
            keyPositions.append((tempVarTwo, lengthGrid - tempVarTwo - 1))
            tempVarTwo += 1

        tempVarThree = middleIndex
        while True:
            keyPositions.append((tempVarThree, middleIndex))
            tempVarThree += 1
            if tempVarThree > lengthGrid - 1:
                break

        countedKeyVals = accumulateCounts(keyPositions, grid)

        allPositions = []
        outerIdx = 0
        while outerIdx < lengthGrid:
            innerIdx_j = 0
            while innerIdx_j < lengthGrid:
                allPositions.append((outerIdx, innerIdx_j))
                innerIdx_j += 1
            outerIdx += 1

        outsideKeyPositions = []
        for tupPos in allPositions:
            found = False
            for keyPos in keyPositions:
                if tupPos[0] == keyPos[0] and tupPos[1] == keyPos[1]:
                    found = True
                    break
            if not found:
                outsideKeyPositions.append(tupPos)

        countedNonKeyVals = accumulateCounts(outsideKeyPositions, grid)

        minOps = 10**9  # sufficiently large number as positive infinity substitute

        yValIter = 0
        while yValIter <= 2:
            nonYValIter = 0
            while nonYValIter <= 2:
                if yValIter != nonYValIter:
                    sumYCounts = sum(countedKeyVals.values())
                    sumNonYCounts = sum(countedNonKeyVals.values())
                    opsCurr = (sumYCounts - countedKeyVals.get(yValIter, 0)) + (sumNonYCounts - countedNonKeyVals.get(nonYValIter, 0))
                    if opsCurr < minOps:
                        minOps = opsCurr
                nonYValIter += 1
            yValIter += 1

        return minOps