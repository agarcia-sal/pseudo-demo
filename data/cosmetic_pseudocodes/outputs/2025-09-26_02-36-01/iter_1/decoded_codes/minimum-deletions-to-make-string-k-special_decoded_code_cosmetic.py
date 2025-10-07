class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqDict = {}
        for character in word:
            freqDict[character] = freqDict.get(character, 0) + 1

        freqList = sorted(freqDict.values())
        bestDeletionCount = float('inf')

        for i in range(len(freqList)):
            capFrequency = freqList[i] + k
            currentDeletionCount = 0

            for j in range(i + 1, len(freqList)):
                if freqList[j] > capFrequency:
                    currentDeletionCount += freqList[j] - capFrequency

            for j in range(i):
                currentDeletionCount += freqList[j]

            if currentDeletionCount < bestDeletionCount:
                bestDeletionCount = currentDeletionCount

        return bestDeletionCount