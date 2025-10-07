class Solution:
    def minValidStrings(self, words, target):
        seenPrefixes = set()
        for currentWord in words:
            idx2 = 0
            while idx2 < len(currentWord):
                idx2 += 1
                tempSubstring = currentWord[:idx2]
                seenPrefixes.add(tempSubstring)

        sizeTarget = len(target)
        resultList = [float('inf')] * (sizeTarget + 1)
        resultList[0] = 0

        for idx1 in range(1, sizeTarget + 1):
            for idx2 in range(1, idx1 + 1):
                subStrBuilder = target[idx2 - 1:idx1]
                if subStrBuilder in seenPrefixes:
                    candidate = resultList[idx2 - 1] + 1
                    if candidate < resultList[idx1]:
                        resultList[idx1] = candidate

        return resultList[sizeTarget] if resultList[sizeTarget] != float('inf') else -1