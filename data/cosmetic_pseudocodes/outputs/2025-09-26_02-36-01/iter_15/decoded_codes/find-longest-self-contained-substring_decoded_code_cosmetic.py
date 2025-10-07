class Solution:
    def maxSubstringLength(self, s: str) -> int:
        alphaFreq = {}
        for ch in s:
            alphaFreq[ch] = alphaFreq.get(ch, 0) + 1

        bestLen = -1
        n = len(s)

        for outerIdx in range(n):
            subFreq = {}
            innerIdx = outerIdx
            while innerIdx < n:
                curChar = s[innerIdx]
                subFreq[curChar] = subFreq.get(curChar, 0) + 1

                validSub = True
                for keyChar in subFreq:
                    if subFreq[keyChar] < alphaFreq.get(keyChar, 0):
                        validSub = False
                        break

                if validSub and len(subFreq) < len(alphaFreq):
                    candidateLen = innerIdx - outerIdx + 1
                    if candidateLen > bestLen:
                        bestLen = candidateLen

                innerIdx += 1

        return bestLen