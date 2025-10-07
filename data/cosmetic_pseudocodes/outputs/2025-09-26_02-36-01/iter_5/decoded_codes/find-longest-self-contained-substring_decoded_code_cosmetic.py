class Solution:
    def maxSubstringLength(self, s: str) -> int:
        def countFrequency(str_, pos, freqMap):
            if pos == len(str_):
                return freqMap
            updatedFreq = freqMap.copy()
            currentChar = str_[pos]
            updatedFreq[currentChar] = updatedFreq.get(currentChar, 0) + 1
            return countFrequency(str_, pos + 1, updatedFreq)

        totalFreq = countFrequency(s, 0, {})
        resultLen = -1

        def checkContains(currentFreq, totalFreqKeys, keyIndex):
            if keyIndex == len(totalFreqKeys):
                return True
            currentKey = totalFreqKeys[keyIndex]
            if currentFreq.get(currentKey, 0) < totalFreq[currentKey]:
                return False
            return checkContains(currentFreq, totalFreqKeys, keyIndex + 1)

        def explore(i, maxLen):
            if i == len(s):
                return maxLen

            def innerExplore(j, currentFreq, curMax):
                if j == len(s):
                    return curMax
                charAtJ = s[j]
                updatedCurrentFreq = currentFreq.copy()
                updatedCurrentFreq[charAtJ] = updatedCurrentFreq.get(charAtJ, 0) + 1

                keysCurrentFreq = list(updatedCurrentFreq.keys())
                keysTotalFreq = list(totalFreq.keys())
                conditionHolds = checkContains(updatedCurrentFreq, keysCurrentFreq, 0)

                if conditionHolds:
                    diffCount = len(keysCurrentFreq) - len(keysTotalFreq)
                    if diffCount < 0:
                        diffLen = (j - i) + 1
                        if diffLen > curMax:
                            curMax = diffLen

                return innerExplore(j + 1, updatedCurrentFreq, curMax)

            updatedMaxLen = innerExplore(i, {}, maxLen)
            return explore(i + 1, updatedMaxLen)

        finalResult = explore(0, resultLen)
        return finalResult