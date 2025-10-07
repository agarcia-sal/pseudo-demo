from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        def swapSortAsc(arr: List[int]) -> None:
            idxA = 0
            n = len(arr)
            while idxA < n - 1:
                idxB = 0
                while idxB < n - idxA - 1:
                    if not (arr[idxB] <= arr[idxB + 1]):
                        arr[idxB], arr[idxB + 1] = arr[idxB + 1], arr[idxB]
                    idxB += 1
                idxA += 1

        swapSortAsc(enemyEnergies)

        if currentEnergy < enemyEnergies[0]:
            return 0

        totalPointsAccumulated = 0

        def loopBackwards(index: int) -> None:
            nonlocal currentEnergy, totalPointsAccumulated
            if index < 0:
                return
            pointsGained = currentEnergy // enemyEnergies[0]
            remainderEnergy = currentEnergy - pointsGained * enemyEnergies[0]
            currentEnergy = remainderEnergy + enemyEnergies[index]
            totalPointsAccumulated += pointsGained
            loopBackwards(index - 1)

        loopBackwards(len(enemyEnergies) - 1)
        return totalPointsAccumulated