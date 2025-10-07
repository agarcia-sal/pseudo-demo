class Solution:
    def maxSubstringLength(self, s: str) -> int:
        def countChars(string: str) -> dict:
            freqMap = {}
            idx = 0
            while idx < len(string):
                ch = string[idx]
                if ch in freqMap:
                    freqMap[ch] += 1
                else:
                    freqMap[ch] = 1
                idx += 1
            return freqMap

        totalFrequencies = countChars(s)
        resultLength = -1
        startIdx = 0

        while startIdx < len(s):
            runningFreq = {}

            def checkCoverage(freqA: dict, freqB: dict) -> bool:
                def keysList(map_: dict) -> list:
                    keysArr = []
                    for key in map_:
                        keysArr.append(key)
                    return keysArr

                keySet = keysList(freqA)
                pos = 0
                while pos < len(keySet):
                    k = keySet[pos]
                    if k not in freqB or freqA[k] < freqB[k]:
                        return False
                    pos += 1
                return True

            def keyCount(map_: dict) -> int:
                countVar = 0
                for _ in map_:
                    countVar += 1
                return countVar

            endIdx = startIdx
            while endIdx < len(s):
                currentChar = s[endIdx]
                if currentChar in runningFreq:
                    runningFreq[currentChar] += 1
                else:
                    runningFreq[currentChar] = 1

                fullCoverage = checkCoverage(runningFreq, totalFrequencies)

                if fullCoverage and keyCount(runningFreq) < keyCount(totalFrequencies):
                    currentLength = endIdx - startIdx + 1
                    if resultLength < currentLength:
                        resultLength = currentLength
                endIdx += 1

            startIdx += 1

        return resultLength