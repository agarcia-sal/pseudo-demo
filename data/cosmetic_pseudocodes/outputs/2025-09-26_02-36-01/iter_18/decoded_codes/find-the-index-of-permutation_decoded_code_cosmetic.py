class Solution:
    def getPermutationIndex(self, perm):
        lengthCounter = len(perm)
        modulusValue = 10**9 + 1

        factorialArray = [1] * lengthCounter
        tracker = 2
        while tracker <= lengthCounter - 1:
            factorialArray[tracker] = factorialArray[tracker - 1] * tracker
            tracker += 1

        availableNumbers = []
        fillIndex = 1
        while fillIndex <= lengthCounter:
            availableNumbers.append(fillIndex)
            fillIndex += 1

        finalIndex = 0
        loopPointer = 0
        while loopPointer < lengthCounter:
            currentElement = perm[loopPointer]
            locationIndex = 0
            while locationIndex < len(availableNumbers):
                if availableNumbers[locationIndex] == currentElement:
                    break
                locationIndex += 1

            multiplierValue = factorialArray[lengthCounter - loopPointer - 1]
            finalIndex += locationIndex * multiplierValue
            del availableNumbers[locationIndex]

            loopPointer += 1

        remainderResult = finalIndex % modulusValue
        return remainderResult