class Solution:
    def maxSubstringLength(self, s: str) -> int:
        def buildFrequencyMap(string: str) -> dict:
            freqMap = {}
            k = 0
            while k < len(string):
                freqMap[string[k]] = freqMap.get(string[k], 0) + 1
                k += 1
            return freqMap

        fullFreq = buildFrequencyMap(s)
        maximumLength = -1
        outerIndex = 0
        while outerIndex <= len(s) - 1:
            partialFreq = {}
            innerIndex = outerIndex
            while innerIndex <= len(s) - 1:
                currentChar = s[innerIndex]
                partialFreq[currentChar] = partialFreq.get(currentChar, 0) + 1
                selfContainedFlag = True
                freqCharKeys = list(partialFreq.keys())
                k = 0
                while k < len(freqCharKeys):
                    ch = freqCharKeys[k]
                    if partialFreq[ch] < fullFreq[ch]:
                        selfContainedFlag = False
                        break
                    k += 1
                if selfContainedFlag and len(partialFreq) < len(fullFreq):
                    currentLength = innerIndex - outerIndex + 1
                    if maximumLength < currentLength:
                        maximumLength = currentLength
                innerIndex += 1
            outerIndex += 1
        return maximumLength