from collections import defaultdict

class Solution:
    def maxDifference(self, s, k):
        finalDiff = -10**10
        charPairs = []
        baseChars = ["zero", "one", "two", "three", "four"]
        n = len(baseChars)
        for idxX in range(n - 1):
            for idxY in range(idxX + 1, n):
                firstChar = baseChars[idxX]
                secondChar = baseChars[idxY]
                charPairs.append([firstChar, secondChar])
                charPairs.append([secondChar, firstChar])

        for pair in charPairs:
            firstTarget, secondTarget = pair
            lowerBounds = defaultdict(lambda: 10**10)
            prefixCountA = [0]
            prefixCountB = [0]
            leftIndex = 0

            for index, char in enumerate(s):
                prevCountA = prefixCountA[-1]
                prevCountB = prefixCountB[-1]

                newCountA = prevCountA + 1 if char == firstTarget else 0
                prefixCountA.append(newCountA)

                newCountB = prevCountB + 1 if char == secondTarget else 0
                prefixCountB.append(newCountB)

                while True:
                    windowLength = (index + 1) - leftIndex
                    prefixAAtLeft = prefixCountA[leftIndex]
                    prefixBAtLeft = prefixCountB[leftIndex]
                    prefixALast = prefixCountA[-1]
                    prefixBLast = prefixCountB[-1]

                    if windowLength < k:
                        break
                    if prefixAAtLeft >= prefixALast:
                        break
                    if prefixBAtLeft >= prefixBLast:
                        break

                    parityPair = (prefixAAtLeft % 2, prefixBAtLeft % 2)
                    candidateVal = prefixAAtLeft - prefixBAtLeft
                    if candidateVal < lowerBounds[parityPair]:
                        lowerBounds[parityPair] = candidateVal
                    leftIndex += 1

                currentParity = ((1 - (prefixALast % 2)), (prefixBLast % 2))
                potentialDiff = prefixALast - prefixBLast - lowerBounds[currentParity]
                if potentialDiff > finalDiff:
                    finalDiff = potentialDiff

        return finalDiff