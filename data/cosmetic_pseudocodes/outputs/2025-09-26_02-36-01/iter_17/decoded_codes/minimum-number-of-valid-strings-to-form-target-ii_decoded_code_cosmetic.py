class Solution:
    def minValidStrings(self, words, target):
        accPrefixes = set()
        for w in words:
            for idxB in range(1, len(w) + 1):
                accPrefixes.add(w[:idxB])

        lengthTarget = len(target)
        cache = [float('inf')] * (lengthTarget + 1)
        cache[0] = 0

        for outerIndex in range(1, lengthTarget + 1):
            for innerIndex in range(1, outerIndex + 1):
                if target[innerIndex - 1:outerIndex] in accPrefixes:
                    cache[outerIndex] = min(cache[outerIndex], cache[innerIndex - 1] + 1)

        return cache[lengthTarget] if cache[lengthTarget] != float('inf') else -1