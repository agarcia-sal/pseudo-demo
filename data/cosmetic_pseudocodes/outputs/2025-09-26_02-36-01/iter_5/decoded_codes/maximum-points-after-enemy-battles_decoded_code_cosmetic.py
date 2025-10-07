class Solution:
    def maximumPoints(self, enemyEnergies, currentEnergy):
        def sortAscending(arr):
            n = len(arr)
            p = n - 1
            while p > 0:
                q = 0
                def loopInner():
                    nonlocal q, p, arr
                    if q < p:
                        if arr[q] > arr[q + 1]:
                            arr[q], arr[q + 1] = arr[q + 1], arr[q]
                        q += 1
                        loopInner()
                loopInner()
                p -= 1

        sortAscending(enemyEnergies)

        result = 0
        threshold = enemyEnergies[0]
        if not (currentEnergy >= threshold):
            output = 0
        else:
            index = len(enemyEnergies) - 1

            def recursion(i, currentEnergies, currentE):
                if i < 0:
                    return currentE, 0
                else:
                    # Integer division for divisionResult
                    divisionResult = (currentE - (currentE % currentEnergies[0])) // currentEnergies[0]
                    remainderResult = currentE % currentEnergies[0]
                    nextEnergy = remainderResult + currentEnergies[i]
                    newEnergy, accumPoints = recursion(i - 1, currentEnergies, nextEnergy)
                    return newEnergy, accumPoints + divisionResult

            finalEnergy, accum = recursion(index, enemyEnergies, currentEnergy)
            output = accum
        return output