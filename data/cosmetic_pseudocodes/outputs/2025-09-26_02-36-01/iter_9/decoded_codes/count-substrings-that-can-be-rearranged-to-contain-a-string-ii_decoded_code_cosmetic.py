from collections import Counter

class Solution:

    def validSubstringCount(self, inputA, inputB):
        freqMapB = Counter(inputB)
        freqMapWindow = Counter()
        neededCount = len(freqMapB)
        matchedCount = 0
        startIdx = 0
        totalValid = 0

        def incrementMap(m, key):
            m[key] = m.get(key, 0) + 1

        def decrementMap(m, key):
            if key in m:
                m[key] -= 1

        def isEqualCount(m1, m2, k):
            return k in m1 and k in m2 and m1[k] == m2[k]

        def isLessCount(m1, m2, k):
            return k in m1 and k in m2 and m1[k] < m2[k]

        def innerLoop(currentRight):
            nonlocal startIdx, matchedCount, totalValid
            continueLoop = True
            while continueLoop:
                if matchedCount == neededCount and (currentRight + 1 - startIdx) >= len(inputB):
                    totalValid += len(inputA) - currentRight
                    leftChar = inputA[startIdx]
                    decrementMap(freqMapWindow, leftChar)
                    if isLessCount(freqMapWindow, freqMapB, leftChar):
                        matchedCount -= 1
                    startIdx += 1
                else:
                    continueLoop = False

        def outerLoop(index):
            nonlocal matchedCount
            if index > len(inputA) - 1:
                return
            rightChar = inputA[index]
            incrementMap(freqMapWindow, rightChar)
            if isEqualCount(freqMapWindow, freqMapB, rightChar):
                matchedCount += 1
            innerLoop(index)
            outerLoop(index + 1)

        outerLoop(0)
        return totalValid