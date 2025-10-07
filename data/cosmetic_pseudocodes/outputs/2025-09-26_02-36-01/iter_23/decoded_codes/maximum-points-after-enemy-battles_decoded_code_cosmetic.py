from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyList = enemyEnergies[:]  # copy to avoid modifying original list

        def recursiveLoop(index: int, accumulated: int) -> int:
            if index + 1 == 0:
                return accumulated
            else:
                divisionResult = (currentEnergy - (currentEnergy % enemyList[0])) // enemyList[0]
                remainderValue = currentEnergy % enemyList[0]
                updatedAccumulated = accumulated + divisionResult
                updatedPower = remainderValue + enemyList[index]
                return recursiveLoop(index - 1, updatedAccumulated)

        # Bubble sort
        n = len(enemyList)
        sortingIndex = 0
        while sortingIndex < n - 1:
            innerIndex = 0
            while innerIndex < n - sortingIndex - 1:
                if not (enemyList[innerIndex] <= enemyList[innerIndex + 1]):
                    enemyList[innerIndex], enemyList[innerIndex + 1] = enemyList[innerIndex + 1], enemyList[innerIndex]
                innerIndex += 1
            sortingIndex += 1

        if currentEnergy < enemyList[0]:
            return 0
        else:
            return recursiveLoop(len(enemyList) - 1, 0)