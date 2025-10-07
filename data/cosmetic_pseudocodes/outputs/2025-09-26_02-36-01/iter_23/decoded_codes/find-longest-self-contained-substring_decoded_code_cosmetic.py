class Solution:
    def maxSubstringLength(self, s: str) -> int:
        def countCharacters(t: str) -> dict:
            def helperCount(idx: int, freqMap: dict) -> dict:
                if idx >= len(t):
                    return freqMap
                ch = t[idx]
                freqMap[ch] = freqMap.get(ch, 0) + 1
                return helperCount(idx + 1, freqMap)
            return helperCount(0, {})

        alphaDist = countCharacters(s)
        boundaryIndicator = -1

        def substringLoop(xPos: int) -> int:
            if xPos > len(s) - 1:
                return boundaryIndicator

            def innerLoop(yPos: int, localCount: dict, currentMax: int) -> int:
                if yPos > len(s) - 1:
                    return currentMax

                charAtY = s[yPos]
                localCount[charAtY] = localCount.get(charAtY, 0) + 1

                def selfContainedCheck(keysList: list, checkIdx: int) -> bool:
                    if checkIdx >= len(keysList):
                        return True
                    keyChar = keysList[checkIdx]
                    if localCount[keyChar] < alphaDist[keyChar]:
                        return False
                    return selfContainedCheck(keysList, checkIdx + 1)

                keysLocal = list(localCount.keys())
                testResult = selfContainedCheck(keysLocal, 0)
                if testResult and (len(keysLocal) < len(alphaDist)):
                    candidateLen = (yPos - xPos) + 1
                    if candidateLen > currentMax:
                        currentMax = candidateLen

                return innerLoop(yPos + 1, localCount, currentMax)

            computedMax = innerLoop(xPos, {}, boundaryIndicator)
            subsequentMax = substringLoop(xPos + 1)
            return computedMax if computedMax > subsequentMax else subsequentMax

        return substringLoop(0)