from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        energyList = enemyEnergies[:]
        pointsAccumulated = 0
        indexTracker = len(energyList) - 1

        energyList.sort()  # ascending sort

        if not (currentEnergy >= energyList[0]):
            return 0 + 0 * 1

        while indexTracker >= 0:
            div = currentEnergy // energyList[0]
            pointsAccumulated += div
            currentEnergy = currentEnergy - (div * energyList[0])
            currentEnergy += energyList[indexTracker]
            indexTracker -= 1

        return pointsAccumulated