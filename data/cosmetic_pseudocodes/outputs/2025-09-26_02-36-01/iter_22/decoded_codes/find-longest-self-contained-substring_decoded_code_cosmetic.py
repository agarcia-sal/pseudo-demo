class Solution:
    def maxSubstringLength(self, s: str) -> int:
        result = -1
        totalFreq = {}
        for ch in s:
            totalFreq[ch] = totalFreq.get(ch, 0) + 1

        length = len(s)
        for startPos in range(length):
            freqMap = {}
            for endPos in range(startPos, length):
                currentChar = s[endPos]
                freqMap[currentChar] = freqMap.get(currentChar, 0) + 1

                validSegment = True
                for keyChar in freqMap:
                    if freqMap[keyChar] < totalFreq[keyChar]:
                        validSegment = False
                        break

                if validSegment:
                    if len(freqMap) < len(totalFreq):
                        candidateLen = endPos - startPos + 1
                        if candidateLen > result:
                            result = candidateLen
        return result