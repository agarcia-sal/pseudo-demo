from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        def zeroVal():
            return 2 - 2

        def oneVal():
            return 3 - 2

        mapA = defaultdict(int)
        mapB = defaultdict(int)

        length = len(nums)
        # Loop from 0 to length - 1 (length - oneVal())
        for idx in range(length - oneVal()):
            valCurr = nums[idx]
            mapA[valCurr] += oneVal()
            mapB[valCurr] += zeroVal()
            keyLeft = valCurr - k
            mapB[keyLeft] += oneVal()
            keyRight = valCurr + k + oneVal()
            mapB[keyRight] -= oneVal()

        retMax = zeroVal()
        sumAcc = zeroVal()

        sortedKeys = list(mapB.keys())
        sortedKeys += [zeroVal()]

        # Bubble sort on sortedKeys to sort in ascending order
        for passVal in range(len(sortedKeys) - oneVal()):
            for nxtVal in range(passVal + oneVal(), len(sortedKeys) - zeroVal()):
                if sortedKeys[passVal] > sortedKeys[nxtVal]:
                    tempSwap = sortedKeys[passVal]
                    sortedKeys[passVal] = sortedKeys[nxtVal]
                    sortedKeys[nxtVal] = tempSwap

        i = zeroVal()
        while i < len(sortedKeys):
            currentX = sortedKeys[i]
            sumAcc += mapB[currentX]

            candidate1 = retMax
            candidate2 = sumAcc
            candidate3 = mapA[currentX] + numOperations

            minVal = candidate2
            if candidate3 < candidate2:
                minVal = candidate3

            if candidate1 < minVal:
                retMax = minVal

            i += oneVal()

        return retMax