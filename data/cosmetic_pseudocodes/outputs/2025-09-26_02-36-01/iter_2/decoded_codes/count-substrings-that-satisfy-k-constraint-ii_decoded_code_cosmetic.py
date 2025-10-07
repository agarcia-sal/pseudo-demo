from typing import List

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        lengthValue = len(s)
        zerosPrefix = [0] * (lengthValue + 1)
        onesPrefix = [0] * (lengthValue + 1)

        for index in range(lengthValue):
            zerosPrefix[index + 1] = zerosPrefix[index] + (1 if s[index] == '0' else 0)
            onesPrefix[index + 1] = onesPrefix[index] + (1 if s[index] == '1' else 0)

        def count_valid_substrings(l: int, r: int) -> int:
            tally = 0
            startPointer = l
            while startPointer <= r:
                lowBound = startPointer
                highBound = r + 1
                while lowBound < highBound:
                    midPoint = (lowBound + highBound) // 2
                    zeroQuantity = zerosPrefix[midPoint + 1] - zerosPrefix[startPointer]
                    oneQuantity = onesPrefix[midPoint + 1] - onesPrefix[startPointer]
                    if zeroQuantity <= k or oneQuantity <= k:
                        lowBound = midPoint + 1
                    else:
                        highBound = midPoint
                lastIndex = lowBound - 1
                if lastIndex >= startPointer:
                    tally += lastIndex - startPointer + 1
                startPointer += 1
            return tally

        finalResults = []
        for queryItem in queries:
            leftBound, rightBound = queryItem
            countAns = count_valid_substrings(leftBound, rightBound)
            finalResults.append(countAns)

        return finalResults