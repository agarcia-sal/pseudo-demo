class Solution:
    def maximumPoints(self, enemyEnergies, currentEnergy):
        sortedList = sorted(enemyEnergies)
        totalPoints = 0
        if currentEnergy < sortedList[0]:
            return 0
        idx = len(sortedList)
        while idx > 0:
            idx -= 1
            divisionResult = currentEnergy // sortedList[0]
            totalPoints += divisionResult
            remainderEnergy = currentEnergy - divisionResult * sortedList[0]
            currentEnergy = remainderEnergy + sortedList[idx]
        return totalPoints