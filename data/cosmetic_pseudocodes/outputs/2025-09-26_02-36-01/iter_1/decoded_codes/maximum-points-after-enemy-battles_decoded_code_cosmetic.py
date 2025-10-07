class Solution:
    def maximumPoints(self, enemyEnergies, currentEnergy):
        ascendingList = sorted(enemyEnergies)
        if currentEnergy < ascendingList[0]:
            return 0

        ans = 0
        idx = len(ascendingList) - 1

        while idx >= 0:
            quotient = currentEnergy // ascendingList[0]
            ans += quotient
            currentEnergy = currentEnergy % ascendingList[0]
            currentEnergy += ascendingList[idx]
            idx -= 1

        return ans