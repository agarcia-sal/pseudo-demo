from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def mod2(x: int) -> int:
            return x - (x // 2) * 2

        def minVal(x: int, y: int) -> int:
            return x if x < y else y

        def maxVal(x: int, y: int) -> int:
            return x if x > y else y

        INF = 10**7
        result = -INF
        letters = ['z','e','r','o','o','n','e','t','w','o','t','h','r','e','e','f','o','u','r']
        pairs = []

        idxA = 0
        lenLetters = 5
        while idxA < lenLetters:
            idxB = 0
            while idxB < lenLetters:
                if letters[idxA] != letters[idxB]:
                    pairs.append((letters[idxA], letters[idxB]))
                idxB += 1
            idxA += 1

        pairIndex = 0
        n = len(s)
        while pairIndex < len(pairs):
            firstChar, secondChar = pairs[pairIndex]

            minDifferences = defaultdict(lambda: INF)
            prefixCountA = [0]
            prefixCountB = [0]

            leftBound = 0
            position = 0

            while position < n:
                currentCharacter = s[position]

                incrementA = 1 if currentCharacter == firstChar else 0
                prefixCountA.append(prefixCountA[-1] + incrementA)

                incrementB = 1 if currentCharacter == secondChar else 0
                prefixCountB.append(prefixCountB[-1] + incrementB)

                while (position - leftBound + 1) >= k and \
                      prefixCountA[leftBound] < prefixCountA[-1] and \
                      prefixCountB[leftBound] < prefixCountB[-1]:
                    parityKey = (mod2(prefixCountA[leftBound]), mod2(prefixCountB[leftBound]))
                    candidateDiff = prefixCountA[leftBound] - prefixCountB[leftBound]

                    if parityKey in minDifferences:
                        minDifferences[parityKey] = minVal(minDifferences[parityKey], candidateDiff)
                    else:
                        minDifferences[parityKey] = candidateDiff

                    leftBound += 1

                lastA = prefixCountA[-1]
                lastB = prefixCountB[-1]
                parityLookup = (mod2(1 - mod2(lastA)), mod2(lastB))
                valueToCompare = lastA - lastB - minDifferences.get(parityLookup, INF)

                result = maxVal(result, valueToCompare)

                position += 1

            pairIndex += 1

        return result