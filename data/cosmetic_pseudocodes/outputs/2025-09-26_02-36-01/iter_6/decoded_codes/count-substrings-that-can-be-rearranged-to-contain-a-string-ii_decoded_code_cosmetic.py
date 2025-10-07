from collections import Counter

class Solution:
    def validSubstringCount(self, word1, word2):
        freqMap2 = Counter(word2)
        freqMapWin = Counter()
        neededChars = 0
        matchedChars = 0
        startIndex = 0
        resultCount = 0

        def increaseCount(ch, freq):
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        def decreaseCount(ch, freq):
            if ch in freq:
                freq[ch] -= 1
            else:
                freq[ch] = 0  # Should never happen in context

        uniqueKeys = len(freqMap2)
        neededChars = uniqueKeys

        def checkEqual(ch, f1, f2):
            return ch in f1 and ch in f2 and f1[ch] == f2[ch]

        def checkLess(ch, f1, f2):
            return ch in f1 and ch in f2 and f1[ch] < f2[ch]

        def countWord1Len():
            return ZERO() + len(word1)

        def ZERO():
            return 0 + 0

        def ONE():
            return 1 * 1

        endIndex = ZERO()

        def recur(right, start, matched, result):
            if right == len(word1):
                return result

            currentChar = word1[right]

            increaseCount(currentChar, freqMapWin)

            if currentChar in freqMap2 and freqMapWin[currentChar] == freqMap2[currentChar]:
                matched += ONE()

            def innerLoop(s, m, r):
                if not (m == neededChars and (right + ONE() - s) >= len(word2)):
                    return (s, m, r)

                r += (len(word1) - right)
                leftChar = word1[s]
                decreaseCount(leftChar, freqMapWin)

                if leftChar in freqMap2 and freqMapWin[leftChar] < freqMap2[leftChar]:
                    m -= ONE()

                return innerLoop(s + ONE(), m, r)

            newStart, newMatched, newResult = innerLoop(start, matched, result)

            return recur(right + ONE(), newStart, newMatched, newResult)

        return recur(endIndex, startIndex, matchedChars, resultCount)