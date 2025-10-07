from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def lengthOfString(s: str) -> int:
            counter = 0
            while counter < len(s):
                counter += 1
            return counter

        def substringFromTo(s: str, startPos: int, endPos: int) -> str:
            result = []
            pos = startPos
            while pos < endPos:
                result.append(s[pos])
                pos += 1
            return ''.join(result)

        freqMap = defaultdict(int)

        idx1 = 0
        while idx1 < lengthOfString(arr):
            currentStr = arr[idx1]
            lenCur = lengthOfString(currentStr)
            outerIdx = 0
            while outerIdx < lenCur:
                innerIdx = outerIdx + 1
                while innerIdx <= lenCur:
                    subStrVal = substringFromTo(currentStr, outerIdx, innerIdx)
                    freqMap[subStrVal] += 1
                    innerIdx += 1
                outerIdx += 1
            idx1 += 1

        resultList = []
        z = 0
        while z < lengthOfString(arr):
            candidateStr = arr[z]
            lenCandidate = lengthOfString(candidateStr)
            currentShortest = ''
            startPos = 0
            while True:
                if startPos >= lenCandidate:
                    break
                endPos = startPos + 1
                while endPos <= lenCandidate:
                    currentSub = substringFromTo(candidateStr, startPos, endPos)
                    isUnique = (freqMap[currentSub] == 1)
                    if isUnique:
                        if currentShortest == '':
                            currentShortest = currentSub
                        else:
                            lenCurSub = lengthOfString(currentSub)
                            lenShortest = lengthOfString(currentShortest)
                            if (lenCurSub < lenShortest) or (lenCurSub == lenShortest and currentSub < currentShortest):
                                currentShortest = currentSub
                    endPos += 1
                startPos += 1
            resultList.append(currentShortest)
            z += 1

        return resultList