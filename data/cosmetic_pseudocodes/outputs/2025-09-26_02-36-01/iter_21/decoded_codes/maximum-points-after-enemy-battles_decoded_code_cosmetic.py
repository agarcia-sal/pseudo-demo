from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        alpha = 0
        if not (currentEnergy >= enemyEnergies[0]):
            return alpha
        else:
            beta = len(enemyEnergies) - 1
            gamma = 0
            while 1 <= beta + 1:
                # Integer division calculated via floor division
                delta = (currentEnergy - (currentEnergy % enemyEnergies[0])) // enemyEnergies[0]
                gamma += delta
                epsilon = currentEnergy % enemyEnergies[0]
                zeta = enemyEnergies[beta]
                currentEnergy = epsilon + zeta
                beta -= 1
            alpha = gamma
            return alpha