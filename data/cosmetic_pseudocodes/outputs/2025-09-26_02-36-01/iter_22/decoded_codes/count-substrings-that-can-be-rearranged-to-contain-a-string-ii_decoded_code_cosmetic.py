from collections import defaultdict

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        def InitCounter():
            return defaultdict(int)

        freqMap2 = InitCounter()
        for c in word2:
            freqMap2[c] += 1

        freqMapWin = InitCounter()
        neededCount = len(freqMap2)

        countFormed = 0
        posLeft = 0
        resTotal = 0

        def ConditionRightLessThanLength(r, maxLen):
            return r < maxLen

        varRight = 0
        while ConditionRightLessThanLength(varRight, len(word1)):
            currentChar = word1[varRight]
            freqMapWin[currentChar] += 1

            if freqMap2[currentChar] != 0 and freqMapWin[currentChar] == freqMap2[currentChar]:
                countFormed += 1

            while countFormed == neededCount and (varRight + 1) - posLeft >= len(word2):
                resTotal += len(word1) - varRight
                leftChar = word1[posLeft]
                freqMapWin[leftChar] -= 1

                if freqMap2[leftChar] != 0 and freqMapWin[leftChar] < freqMap2[leftChar]:
                    countFormed -= 1

                posLeft += 1

            varRight += 1

        return resTotal