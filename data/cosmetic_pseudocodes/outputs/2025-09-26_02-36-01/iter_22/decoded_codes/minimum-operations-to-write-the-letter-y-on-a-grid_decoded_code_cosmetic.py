from collections import defaultdict
from math import inf

class Solution:
    def minimumOperationsToWriteY(self, grid):
        lengthVar = len(grid)
        halfIndex = lengthVar // 2
        coordSet = set()

        indexVar = 0
        while indexVar <= halfIndex:
            coordSet.add((indexVar, indexVar))
            indexVar += 1

        iteratorVar = 0
        while iteratorVar <= halfIndex:
            coordSet.add((iteratorVar, (lengthVar - iteratorVar) - 1))
            iteratorVar += 1

        posVar = halfIndex
        while posVar <= lengthVar - 1:
            coordSet.add((posVar, halfIndex))
            posVar += 1

        def countValuesAtPositions(gridInput, positions):
            countMap = defaultdict(int)
            for rowIter in range(len(gridInput)):
                for colIter in range(len(gridInput[rowIter])):
                    if (rowIter, colIter) in positions:
                        val = gridInput[rowIter][colIter]
                        countMap[val] += 1
            return countMap

        def countValuesNotAtPositions(gridInput, positions):
            countStorage = defaultdict(int)
            for rowIter in range(len(gridInput)):
                for colIter in range(len(gridInput[rowIter])):
                    if (rowIter, colIter) not in positions:
                        elementVal = gridInput[rowIter][colIter]
                        countStorage[elementVal] += 1
            return countStorage

        yCountMap = countValuesAtPositions(grid, coordSet)
        nonYCountMap = countValuesNotAtPositions(grid, coordSet)

        minimalOps = inf
        outerCounter = 0
        while outerCounter <= 2:
            innerCounter = 0
            while innerCounter <= 2:
                if outerCounter != innerCounter:
                    ySum = sum(yCountMap.values())
                    yRemaining = ySum - yCountMap.get(outerCounter, 0)

                    nonYSum = sum(nonYCountMap.values())
                    nonYRemaining = nonYSum - nonYCountMap.get(innerCounter, 0)

                    combinationOps = yRemaining + nonYRemaining
                    if combinationOps < minimalOps:
                        minimalOps = combinationOps
                innerCounter += 1
            outerCounter += 1

        return minimalOps