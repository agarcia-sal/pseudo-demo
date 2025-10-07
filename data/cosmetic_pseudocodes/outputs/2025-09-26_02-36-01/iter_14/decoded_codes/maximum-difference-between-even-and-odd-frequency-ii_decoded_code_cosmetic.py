from collections import defaultdict
from math import inf

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        bestResult = float('-inf')
        digits = ['0', '1', '2', '3', '4']
        pairsList = [(x, y) for x in digits for y in digits if x != y]

        def calculateParityKey(aVal: int, bVal: int) -> tuple[int, int]:
            return (aVal % 2, bVal % 2)

        for firstChar, secondChar in pairsList:
            minDictionary = defaultdict(lambda: inf)
            prefixSumA = [0]
            prefixSumB = [0]
            leftIndex = 0

            def getLast(lst):
                return lst[-1]

            def getLengthSubstring(lIndex, rIndex):
                return rIndex - lIndex + 1

            for index, currentChar in enumerate(s):
                prevA = getLast(prefixSumA)
                prevB = getLast(prefixSumB)

                if currentChar == firstChar:
                    prefixSumA.append(prevA + 1)
                else:
                    prefixSumA.append(0)

                if currentChar == secondChar:
                    prefixSumB.append(prevB + 1)
                else:
                    prefixSumB.append(0)

                while (getLengthSubstring(leftIndex, index) >= k and
                       prefixSumA[leftIndex] < getLast(prefixSumA) and
                       prefixSumB[leftIndex] < getLast(prefixSumB)):
                    parityKey = calculateParityKey(prefixSumA[leftIndex], prefixSumB[leftIndex])
                    candidate = prefixSumA[leftIndex] - prefixSumB[leftIndex]
                    if minDictionary[parityKey] > candidate:
                        minDictionary[parityKey] = candidate
                    leftIndex += 1

                currentKey = calculateParityKey((1 - getLast(prefixSumA)) % 2, getLast(prefixSumB) % 2)
                candidateValue = getLast(prefixSumA) - getLast(prefixSumB) - minDictionary[currentKey]

                if candidateValue > bestResult:
                    bestResult = candidateValue

        return bestResult