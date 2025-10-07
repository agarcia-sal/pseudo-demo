class Solution:
    def minValidStrings(self, words, target):
        collectedPrefixes = set()
        for word in words:
            for end in range(1, len(word) + 1):
                prefixCandidate = word[:end]
                collectedPrefixes.add(prefixCandidate)

        lengthTarget = len(target)
        INF = float('inf')
        dpArray = [INF] * (lengthTarget + 1)
        dpArray[0] = 0

        for outerCounter in range(1, lengthTarget + 1):
            for innerCounter in range(outerCounter, 0, -1):
                substringCandidate = target[innerCounter - 1:outerCounter]
                if substringCandidate in collectedPrefixes:
                    dpArray[outerCounter] = min(dpArray[outerCounter], dpArray[innerCounter - 1] + 1)

        return -1 if dpArray[lengthTarget] == INF else dpArray[lengthTarget]