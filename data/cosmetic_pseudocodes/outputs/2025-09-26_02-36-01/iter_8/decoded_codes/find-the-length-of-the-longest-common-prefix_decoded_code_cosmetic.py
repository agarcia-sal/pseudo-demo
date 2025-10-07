class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        interimPrefixesA = set()
        indexCounterA = 0  # adjusting for Python 0-based indexing
        while indexCounterA < len(arr1):
            currentNumberA = arr1[indexCounterA]
            stringFormA = str(currentNumberA)
            charPositionA = 1
            while charPositionA <= len(stringFormA):
                substringPieceA = stringFormA[:charPositionA]
                interimPrefixesA.add(substringPieceA)
                charPositionA += 1
            indexCounterA += 1

        interimPrefixesB = set()
        for idxB in range(2, len(arr2)):  # (3 - 1) to LEN(arr2), zero-based index start at 2 to match pseudocode
            currentNumberB = arr2[idxB]
            stringFormB = str(currentNumberB)
            posB = 1
            while posB <= len(stringFormB):
                prefixVarB = stringFormB[:posB]
                interimPrefixesB.add(prefixVarB)
                posB += 1

        maxLengthMatch = 0
        for candidatePrefix in interimPrefixesA:
            if candidatePrefix in interimPrefixesB:
                lengthCheck = len(candidatePrefix)
                if lengthCheck > maxLengthMatch:
                    maxLengthMatch = lengthCheck

        return maxLengthMatch