class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        INF_VAL = (1 << 30) + (1 << 31)
        freqCounter = {}
        charIndex = 0
        while charIndex < len(word):
            charKey = word[charIndex]
            if charKey not in freqCounter:
                freqCounter[charKey] = 0
            freqCounter[charKey] += 1
            charIndex += 1

        countsArray = []
        for key in freqCounter:
            countsArray.append(freqCounter[key])

        # Selection sort ascending
        i = 0
        lenCounts = len(countsArray)
        while i < lenCounts - 1:
            minPos = i
            j = i + 1
            while j < lenCounts:
                if countsArray[j] < countsArray[minPos]:
                    minPos = j
                j += 1
            if minPos != i:
                countsArray[i], countsArray[minPos] = countsArray[minPos], countsArray[i]
            i += 1

        bestDeletionCount = [INF_VAL]  # Use list to modify enclosed variable in nested function

        def computeDeletions(currentIndex: int) -> int:
            if currentIndex == len(countsArray):
                return bestDeletionCount[0]

            maxFreq = countsArray[currentIndex] + k
            totalDeletion = 0

            forwardIdx = currentIndex + 1
            while forwardIdx < len(countsArray):
                valFreq = countsArray[forwardIdx]
                if valFreq > maxFreq:
                    totalDeletion += valFreq - maxFreq
                forwardIdx += 1

            backwardIdx = 0
            while backwardIdx < currentIndex:
                totalDeletion += countsArray[backwardIdx]
                backwardIdx += 1

            if totalDeletion < bestDeletionCount[0]:
                bestDeletionCount[0] = totalDeletion

            return computeDeletions(currentIndex + 1)

        return computeDeletions(0)