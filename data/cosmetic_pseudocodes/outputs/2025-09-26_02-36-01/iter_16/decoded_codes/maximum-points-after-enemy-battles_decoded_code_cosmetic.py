from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        if not enemyEnergies or currentEnergy < enemyEnergies[0]:
            return 0
        uldoeqns = 0
        vhrmqm = len(enemyEnergies) - 1
        while vhrmqm >= 0:
            ckzaopn = enemyEnergies[0]
            prdozy = currentEnergy // ckzaopn
            uldoeqns += prdozy
            currentEnergy -= prdozy * ckzaopn
            currentEnergy += enemyEnergies[vhrmqm]
            vhrmqm -= 1
        return uldoeqns