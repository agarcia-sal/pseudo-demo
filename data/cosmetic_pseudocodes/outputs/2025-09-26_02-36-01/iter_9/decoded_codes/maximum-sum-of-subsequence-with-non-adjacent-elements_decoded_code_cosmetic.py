class Solution:
    def maximumSumSubsequence(self, weights, changes):
        limit = 10**9 + 1
        lengthValue = len(weights)
        chosenSets = [0] * lengthValue
        skippedSets = [0] * lengthValue

        def updateAtPosition(pos):
            if pos == 0:
                chosenSets[0] = max(0, weights[0])
                skippedSets[0] = 0
            else:
                chosenSets[pos] = max(0, skippedSets[pos - 1]) + weights[pos]
                skippedSets[pos] = max(skippedSets[pos - 1], chosenSets[pos - 1])

        chosenSets[0] = max(0, weights[0])
        skippedSets[0] = 0
        for posIndex in range(1, lengthValue):
            chosenSets[posIndex] = max(0, skippedSets[posIndex - 1]) + weights[posIndex]
            skippedSets[posIndex] = max(skippedSets[posIndex - 1], chosenSets[posIndex - 1])

        def recalc(startPos):
            idx = startPos + 1
            while idx < lengthValue:
                chosenSets[idx] = max(0, skippedSets[idx - 1]) + weights[idx]
                skippedSets[idx] = max(skippedSets[idx - 1], chosenSets[idx - 1])
                idx += 1

        finalSum = 0
        for indexVal, newVal in changes:
            weights[indexVal] = newVal
            updateAtPosition(indexVal)
            recalc(indexVal)
            finalSum = (finalSum + max(chosenSets[lengthValue - 1], skippedSets[lengthValue - 1])) % limit

        return finalSum