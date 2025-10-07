class Solution:
    def maxSubstringLength(self, s):
        def computeFrequencyMap(sequence):
            mapping = {}
            pos = 0
            while pos < len(sequence):
                charX = sequence[pos]
                if charX in mapping:
                    mapping[charX] = mapping[charX] + 1
                else:
                    mapping[charX] = 1
                pos += 1
            return mapping

        def keysCount(mapM):
            counter = 0
            for _ in mapM:
                counter += 1
            return counter

        def allFreqsAtLeast(freqA, freqB):
            for keyC in freqA:
                if not ((freqA[keyC] >= freqB.get(keyC, 0))):
                    return False
            return True

        totalFreq = computeFrequencyMap(s)
        resultVal = -1

        outerIdx = 0
        while outerIdx < len(s):
            subFreq = {}

            def innerLoop(currentIdx):
                if currentIdx == len(s):
                    return

                ch = s[currentIdx]
                if ch in subFreq:
                    subFreq[ch] = subFreq[ch] + 1
                else:
                    subFreq[ch] = 1

                condition1 = allFreqsAtLeast(subFreq, totalFreq)
                condition2 = keysCount(subFreq) < keysCount(totalFreq)
                if condition1 and condition2:
                    lenCandidate = (currentIdx - outerIdx) + 1
                    nonlocal resultVal
                    if lenCandidate > resultVal:
                        resultVal = lenCandidate

                innerLoop(currentIdx + 1)

            innerLoop(outerIdx)
            outerIdx += 1

        return resultVal