class Solution:
    def maximumPoints(self, enemyEnergies, currentEnergy):
        totalSum = 0
        enemyEnergies.sort()
        if currentEnergy < enemyEnergies[0]:
            return 0
        idx = len(enemyEnergies) - 1
        while idx >= 0:
            divResult = currentEnergy / enemyEnergies[0]
            intDiv = int(divResult)  # intDiv = divResult - (divResult % 1)
            totalSum += intDiv
            currentEnergy -= enemyEnergies[0] * intDiv
            currentEnergy += enemyEnergies[idx]
            idx -= 1
        return totalSum