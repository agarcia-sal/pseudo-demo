class Solution:
    def minValidStrings(self, words, target):
        prefixSet = set()
        for currentWord in words:
            lenWord = len(currentWord)
            # prefix substrings starting at index 1 (0-based index 1 means second character)
            # original pseudocode uses 1-based indexing, here we adjust to Python 0-based indexing
            # substring currentWord[ startPos .. endPos ] with startPos=1 means slice currentWord[1:endPos]
            # endPos goes from 1 to lenWord inclusive
            for subIdx in range(1, lenWord + 1):
                # slice from index 1 up to subIdx (not including subIdx)
                prefixSubstring = currentWord[1:subIdx]  # slice excludes end index, so this is characters from idx 1 to subIdx-1
                prefixSet.add(prefixSubstring)

        targetLen = len(target)
        INF = float('inf')
        dpArr = [INF] * (targetLen + 1)
        dpArr[0] = 0

        # Outer loop from 1 to targetLen (inclusive)
        for outerIndex in range(1, targetLen + 1):
            # innerIndex runs from 1 to outerIndex inclusive
            for innerIndex in range(1, outerIndex + 1):
                # substring target[innerIndex..outerIndex] with 1-based indices means
                # target[innerIndex-1 : outerIndex] in 0-based python indexing
                substrCandidate = target[innerIndex - 1 : outerIndex]
                if substrCandidate in prefixSet:
                    costCandidate = dpArr[innerIndex - 1] + 1
                    if costCandidate < dpArr[outerIndex]:
                        dpArr[outerIndex] = costCandidate

        return dpArr[targetLen] if dpArr[targetLen] != INF else -1