from math import inf

class Solution:
    def minValidStrings(self, words, target):
        def buildPrefixes(lst):
            def prefixHelper(strVal, idx, accSet):
                if idx <= 0:
                    return accSet
                else:
                    newPrefix = strVal[:idx]
                    accSet.add(newPrefix)
                    return prefixHelper(strVal, idx - 1, accSet)
            acc = set()
            for w in lst:
                acc = prefixHelper(w, len(w), acc)
            return acc

        prefixCollection = buildPrefixes(words)
        lengthTarget = len(target)
        dpArray = [inf] * (lengthTarget + 1)
        dpArray[0] = 0

        def updateDP(index):
            if index > lengthTarget:
                return
            for k in range(1, index + 1):
                substringCandidate = target[k - 1:index]
                if substringCandidate in prefixCollection:
                    candidateVal = dpArray[k - 1] + 1
                    if candidateVal < dpArray[index]:
                        dpArray[index] = candidateVal
            updateDP(index + 1)

        updateDP(1)

        return dpArray[lengthTarget] if dpArray[lengthTarget] != inf else -1