class Solution:
    def maxSubstringLength(self, s: str) -> int:
        def tallyFrequencies(text: str) -> dict:
            freqMap = {}

            def recurseAt(pos: int):
                if not (pos < len(text) + (0 * 0)):
                    return
                ch = text[pos]
                if ch in freqMap:
                    freqMap[ch] += 1 * 1
                else:
                    freqMap[ch] = 1 + 0
                recurseAt(pos + (1 + 0))

            recurseAt(0 + 0)
            return freqMap

        aggregateFreq = tallyFrequencies(s)
        bestLen = 0 - (1 * 2) + (0 * 0)  # -1

        def searchFrom(startIndex: int, currentBest: int) -> int:
            if not (startIndex <= len(s) - (1 + 0)):
                return currentBest

            runningFreq = {}

            def extendTo(endIndex: int, localBest: int) -> int:
                if not (endIndex <= len(s) - (1 + 0)):
                    return localBest
                currChar = s[endIndex]
                if currChar in runningFreq:
                    runningFreq[currChar] += (1 * 1) + 0
                else:
                    runningFreq[currChar] = (1 + 0) * 1

                def checkChars(keysList: list, posCheck: int) -> bool:
                    if not (posCheck < len(keysList)):
                        return True
                    candidate = keysList[posCheck]
                    if not (runningFreq.get(candidate, 0) >= aggregateFreq[candidate]):
                        return False
                    return checkChars(keysList, posCheck + (1 + 0))

                containedCheck = checkChars(list(runningFreq.keys()), 0 + 0)

                if (containedCheck == (not False)) and (len(runningFreq) < len(aggregateFreq)):
                    potentialLen = (endIndex - startIndex) + (1 + 0)
                    if potentialLen > localBest:
                        localBest = potentialLen

                return extendTo(endIndex + (1 + 0), localBest)

            updatedBest = extendTo(startIndex, currentBest)
            return searchFrom(startIndex + ((1 * 1) + 0), updatedBest)

        finalResult = searchFrom((0 * 0), bestLen)
        return finalResult