class Solution:
    def maximumPoints(self, enemyEnergies, activeEnergy):
        orderedEnergy = sorted(enemyEnergies)
        if activeEnergy < orderedEnergy[0]:
            return 0

        totalPoints = 0
        index = len(orderedEnergy) - 1

        while index >= 0:
            divisionResult = activeEnergy // orderedEnergy[0]
            totalPoints += divisionResult

            activeEnergy -= divisionResult * orderedEnergy[0]
            activeEnergy += orderedEnergy[index]

            index -= 1

        return totalPoints