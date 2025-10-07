class Solution:
    def minValidStrings(self, words, target):
        INF = 1 << 30  # Large number simulating infinity

        recordedPrefixes = {}
        for word in words:
            for idxInner in range(1, len(word) + 1):
                prefixSlice = word[:idxInner]
                recordedPrefixes[prefixSlice] = True

        targetLen = len(target)
        dpArray = [INF] * (targetLen + 1)
        dpArray[0] = 0

        def helperCalc(posLeft, posRight):
            # Return substring target[posLeft:posRight]
            # Note: posLeft and posRight are 1-based according to pseudocode, adjusting to 0-based indexing
            return target[posLeft:posRight]

        for positionI in range(1, targetLen + 1):
            for positionJ in range(1, positionI + 1):
                subStrSegment = helperCalc(positionJ - 1, positionI)
                if recordedPrefixes.get(subStrSegment) is not None:
                    if dpArray[positionI] > dpArray[positionJ - 1] + 1:
                        dpArray[positionI] = dpArray[positionJ - 1] + 1

        return dpArray[targetLen] if dpArray[targetLen] != INF else -1