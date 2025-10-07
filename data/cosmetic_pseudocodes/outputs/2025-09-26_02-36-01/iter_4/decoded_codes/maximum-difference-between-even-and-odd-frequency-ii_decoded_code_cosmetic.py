from collections import defaultdict
from math import inf

class Solution:
    def maxDifference(self, s: list[str], k: int) -> int:
        result = float('-inf')
        charsSet = ['zero', 'one', 'two', 'three', 'four']
        pairsList = [(charsSet[i], charsSet[j]) for i in range(len(charsSet)) for j in range(len(charsSet)) if i != j]

        for charX, charY in pairsList:
            minDifferences = defaultdict(lambda: float('inf'))
            prefixCountX = [0]
            prefixCountY = [0]
            leftIndex = 0
            index = 0
            n = len(s)

            while index < n:
                currentChar = s[index]
                lastX = prefixCountX[-1]
                lastY = prefixCountY[-1]

                if currentChar == charX:
                    prefixCountX.append(lastX + 1)
                else:
                    prefixCountX.append(0)

                if currentChar == charY:
                    prefixCountY.append(lastY + 1)
                else:
                    prefixCountY.append(0)

                while (index + 1 - leftIndex) >= k and prefixCountX[leftIndex] < prefixCountX[-1] and prefixCountY[leftIndex] < prefixCountY[-1]:
                    parityKey = (prefixCountX[leftIndex] % 2, prefixCountY[leftIndex] % 2)

                    diffCandidate = prefixCountX[leftIndex] - prefixCountY[leftIndex]
                    if diffCandidate < minDifferences[parityKey]:
                        minDifferences[parityKey] = diffCandidate

                    leftIndex += 1

                finalParityKey = ((1 - (prefixCountX[-1] % 2)), (prefixCountY[-1] % 2))
                currentDiff = prefixCountX[-1] - prefixCountY[-1] - minDifferences[finalParityKey]

                if currentDiff > result:
                    result = currentDiff

                index += 1

        return result