class Solution:
    def maximumPoints(self, enemyEnergies, currentEnergy):
        def customSort(array):
            swapped = True
            while swapped:
                swapped = False
                for idx in range(len(array) - 1):
                    if array[idx + 1] < array[idx]:
                        array[idx], array[idx + 1] = array[idx + 1], array[idx]
                        swapped = True

        customSort(enemyEnergies)

        if currentEnergy < enemyEnergies[0]:
            return 0

        accumulator = 0
        pointer = len(enemyEnergies) - 1

        while pointer >= 0:
            divisionResult = currentEnergy // enemyEnergies[0]
            remainderValue = currentEnergy - divisionResult * enemyEnergies[0]
            accumulator += divisionResult
            currentEnergy = remainderValue + enemyEnergies[pointer]
            pointer -= 1

        return accumulator