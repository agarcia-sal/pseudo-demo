class Solution:
    def minValidStrings(self, words, target):
        prefixSet = set()

        def addPrefixes(word):
            for length in range(1, len(word) + 1):
                prefixSet.add(word[:length])

        for word in words:
            addPrefixes(word)

        totalLen = len(target)
        dynArray = [float('inf')] * (totalLen + 1)
        dynArray[0] = 0

        for iVal in range(1, totalLen + 1):
            for jVal in range(1, iVal + 1):
                substrPiece = target[jVal - 1: iVal]
                if substrPiece in prefixSet:
                    tempVal = dynArray[jVal - 1] + 1
                    if tempVal < dynArray[iVal]:
                        dynArray[iVal] = tempVal

        return dynArray[totalLen] if dynArray[totalLen] != float('inf') else -1