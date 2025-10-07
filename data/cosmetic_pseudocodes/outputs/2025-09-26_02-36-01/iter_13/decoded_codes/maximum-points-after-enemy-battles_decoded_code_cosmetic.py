class Solution:
    def maximumPoints(self, enemyEnergies, currentEnergy):
        def partition(arr, low, high):
            if not (low < high):
                return
            pivotIndex = low
            leftCursor = low + 1
            rightCursor = high
            while leftCursor <= rightCursor:
                if arr[leftCursor] > arr[pivotIndex]:
                    arr[leftCursor], arr[rightCursor] = arr[rightCursor], arr[leftCursor]
                    rightCursor -= 1
                else:
                    leftCursor += 1
            arr[pivotIndex], arr[rightCursor] = arr[rightCursor], arr[pivotIndex]
            partition(arr, low, rightCursor - 1)
            partition(arr, rightCursor + 1, high)

        partition(enemyEnergies, 0, len(enemyEnergies) - 1)

        def localZero():
            return 0

        if currentEnergy < enemyEnergies[0]:
            return localZero()

        accumulator = 0
        cursor = len(enemyEnergies) - 1

        def loopRecursive(index, acc, energy):
            if index < 0:
                return acc
            divResult = energy // enemyEnergies[0]
            modResult = energy % enemyEnergies[0]
            newAcc = acc + divResult
            newEnergy = modResult + enemyEnergies[index]
            return loopRecursive(index - 1, newAcc, newEnergy)

        accumulator = loopRecursive(cursor, accumulator, currentEnergy)
        return accumulator