from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], totalEnergy: int) -> int:
        enemyEnergies.sort()
        if totalEnergy < enemyEnergies[0]:
            return 0
        score = 0
        idx = len(enemyEnergies) - 1
        while idx >= 0:
            quotient = totalEnergy // enemyEnergies[0]
            score += quotient
            totalEnergy -= quotient * enemyEnergies[0]
            totalEnergy += enemyEnergies[idx]
            idx -= 1
        return score