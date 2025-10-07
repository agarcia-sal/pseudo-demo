from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        sortedList = sorted(enemyEnergies)
        if not sortedList or currentEnergy < sortedList[0]:
            return 0

        resultCounter = 0
        idx = len(sortedList) - 1

        while idx >= 0:
            divResult = currentEnergy // sortedList[0]
            resultCounter += divResult
            currentEnergy = currentEnergy % sortedList[0]
            currentEnergy += sortedList[idx]
            idx -= 1

        return resultCounter