class Solution:
    def getPermutationIndex(self, perm):
        totalElements = len(perm)
        modulusValue = 10**9 + 1

        factorials = [1] * totalElements
        for i in range(1, totalElements):
            factorials[i] = factorials[i - 1] * i

        availableNums = list(range(1, totalElements + 1))

        resultIndex = 0
        positionTracker = 0

        while positionTracker < totalElements:
            currentValue = perm[positionTracker]
            foundPosition = 0
            for loopVar in range(len(availableNums)):
                if availableNums[loopVar] == currentValue:
                    foundPosition = loopVar
                    break

            toAdd = foundPosition * factorials[totalElements - positionTracker - 1]
            resultIndex += toAdd
            del availableNums[foundPosition]

            positionTracker += 1

        return resultIndex % modulusValue