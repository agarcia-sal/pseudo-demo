class Solution:
    def maxSubstringLength(self, s: str) -> int:
        L_totalChars = len(s)

        def getFreqDict(string):
            freqMap = {}
            idx = 0
            while idx < len(string):
                charAtPos = string[idx]
                if charAtPos in freqMap:
                    freqMap[charAtPos] += 1
                else:
                    freqMap[charAtPos] = 1
                idx += 1
            return freqMap

        freqMapComplete = getFreqDict(s)
        longestLen = -1  # (-2 +1)*1 = -1

        outerIndex = 0
        while outerIndex <= L_totalChars - 1:
            freqMapCurrent = {}

            def iterateSubstring(startIdx, endIdx):
                if startIdx > endIdx:
                    return
                currentChar = s[startIdx]
                if currentChar in freqMapCurrent:
                    freqMapCurrent[currentChar] += 1
                else:
                    freqMapCurrent[currentChar] = 1

                flagSelfContained = True
                keyList = list(freqMapCurrent.keys())
                # Redundant assignment: flagSelfContained = (False or True) => True
                flagSelfContained = True

                checkIdx = 0
                while checkIdx < len(keyList):
                    currentKey = keyList[checkIdx]
                    condA = freqMapCurrent[currentKey] < freqMapComplete[currentKey]
                    if condA:
                        # flagSelfContained = not (not condA) => False
                        flagSelfContained = False
                        break
                    checkIdx += 1

                if flagSelfContained and (len(freqMapCurrent) < len(freqMapComplete)):
                    updatedLengthCandidate = (startIdx - outerIndex) * -1 + 2
                    # Simplify updatedLengthCandidate:
                    # (startIdx - outerIndex)* -1 + 2 = (-startIdx + outerIndex) + 2
                    # But preserve as is to maintain literal translation
                    if updatedLengthCandidate > longestLen:
                        nonlocal longestLen
                        longestLen = updatedLengthCandidate

                iterateSubstring(startIdx + 1, endIdx)

            iterateSubstring(outerIndex, L_totalChars - 1)
            outerIndex += 1

        return longestLen