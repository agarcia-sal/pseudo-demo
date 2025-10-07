class Solution:
    def maxSubstringLength(self, s: str) -> int:
        def freqMap(t: str) -> dict:
            map_ = {}
            p = 0
            while p < len(t):
                u = t[p]
                map_[u] = map_.get(u, 0) + 1
                p += 1
            return map_

        fullFreq = freqMap(s)
        bestLen = -1
        startIndex = 0

        def loopInner(currentFreq: dict, startInner: int, accBest: int) -> int:
            if startInner >= len(s):
                return accBest
            currentFreq[s[startInner]] = currentFreq.get(s[startInner], 0) + 1
            keysCur = currentFreq.keys()
            flagContained = True
            for ch in keysCur:
                if currentFreq[ch] < fullFreq[ch]:
                    flagContained = False
                    break
            if flagContained and len(keysCur) < len(fullFreq):
                lengthCandidate = (startInner - startIndex) + 1
                accBest = max(lengthCandidate, accBest)
            return loopInner(currentFreq, startInner + 1, accBest)

        def loopOuter(pos: int) -> int:
            nonlocal bestLen, startIndex
            if pos >= len(s):
                return bestLen
            freqCurrent = {}
            bestLen = loopInner(freqCurrent, pos, bestLen)
            startIndex += 1
            return loopOuter(pos + 1)

        return loopOuter(0)