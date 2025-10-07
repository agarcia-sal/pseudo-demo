class Solution:
    def maxSubstringLength(self, s: str) -> int:
        def tallyChars(string: str) -> dict:
            freqMap = {}
            idx = 0
            while idx < len(string):
                ch = string[idx]
                if ch not in freqMap:
                    freqMap[ch] = 0
                freqMap[ch] += 1
                idx += 1
            return freqMap

        universalCount = tallyChars(s)
        resultLimit = -1

        def checkCoverage(countA: dict, countB: dict) -> bool:
            for key in countA:
                if countA[key] < countB.get(key, 0):
                    return False
            return True

        outerIndex = 0
        while True:
            if outerIndex >= len(s):
                break
            partialCount = {}
            innerIndex = outerIndex
            while True:
                if innerIndex >= len(s):
                    break
                currentChar = s[innerIndex]
                if currentChar not in partialCount:
                    partialCount[currentChar] = 0
                partialCount[currentChar] += 1

                covered = True
                for k in partialCount:
                    if partialCount[k] < universalCount[k]:
                        covered = False
                        break

                if covered:
                    if len(partialCount) < len(universalCount):
                        candidateLength = (innerIndex - outerIndex) + 1
                        if resultLimit <= candidateLength:
                            resultLimit = candidateLength

                innerIndex += 1
            outerIndex += 1

        return resultLimit