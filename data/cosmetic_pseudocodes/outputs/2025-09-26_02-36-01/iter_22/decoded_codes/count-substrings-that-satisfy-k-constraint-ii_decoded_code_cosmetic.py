from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        length = len(s)
        zerosPrefix = [0] * (length + 1)
        onesPrefix = [0] * (length + 1)

        for idx in range(length):
            zerosPrefix[idx + 1] = zerosPrefix[idx] + (1 if s[idx] == '0' else 0)
            onesPrefix[idx + 1] = onesPrefix[idx] + (1 if s[idx] == '1' else 0)

        def count_valid_substrings(l: int, r: int) -> int:
            totalCount = 0
            currentStart = l
            while currentStart <= r:
                lowBound, highBound = currentStart, r + 1
                while lowBound != highBound:
                    midPos = (lowBound + highBound) // 2
                    zeroSegmentCount = zerosPrefix[midPos + 1] - zerosPrefix[currentStart]
                    oneSegmentCount = onesPrefix[midPos + 1] - onesPrefix[currentStart]
                    if zeroSegmentCount <= k or oneSegmentCount <= k:
                        lowBound = midPos + 1
                    else:
                        highBound = midPos
                lastValid = lowBound - 1
                if lastValid >= currentStart:
                    totalCount += lastValid - currentStart + 1
                currentStart += 1
            return totalCount

        outputList = []
        for l, r in queries:
            outputList.append(count_valid_substrings(l, r))
        return outputList