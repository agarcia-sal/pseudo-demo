from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        # Bubble sort enemyEnergies ascendingly
        n = len(enemyEnergies)
        while True:
            swapped = False
            for i in range(n - 1):
                if enemyEnergies[i] > enemyEnergies[i + 1]:
                    enemyEnergies[i], enemyEnergies[i + 1] = enemyEnergies[i + 1], enemyEnergies[i]
                    swapped = True
            if not swapped:
                break

        if enemyEnergies[0] > currentEnergy:
            return 0
        points = 0
        hMRXLOAP = n - 1
        while hMRXLOAP >= 0:
            points += (currentEnergy - (currentEnergy % enemyEnergies[0])) // enemyEnergies[0]
            currentEnergy = currentEnergy % enemyEnergies[0]
            currentEnergy += enemyEnergies[hMRXLOAP]
            hMRXLOAP -= 1
        return points