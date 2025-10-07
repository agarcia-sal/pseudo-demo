from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        totalLength = len(s)
        zeroPrefixArray = [0] * (totalLength + 1)
        onePrefixArray = [0] * (totalLength + 1)

        def buildPrefixArrays(index: int) -> None:
            if index == totalLength:
                return
            zeroPrefixArray[index + 1] = zeroPrefixArray[index] + (1 if s[index] == '0' else 0)
            onePrefixArray[index + 1] = onePrefixArray[index] + (1 if s[index] == '1' else 0)
            buildPrefixArrays(index + 1)

        buildPrefixArrays(0)

        def count_valid_substrings(leftBound: int, rightBound: int) -> int:
            validSubstringCount = 0

            def loopStart(currentStart: int) -> None:
                nonlocal validSubstringCount
                if currentStart > rightBound:
                    return

                def binarySearch(lowBound: int, highBound: int) -> int:
                    if lowBound >= highBound:
                        return lowBound
                    midPoint = (lowBound + highBound) // 2
                    zeroCountSegment = zeroPrefixArray[midPoint + 1] - zeroPrefixArray[currentStart]
                    oneCountSegment = onePrefixArray[midPoint + 1] - onePrefixArray[currentStart]
                    if zeroCountSegment <= k or oneCountSegment <= k:
                        return binarySearch(midPoint + 1, highBound)
                    else:
                        return binarySearch(lowBound, midPoint)

                maxValidEnd = binarySearch(currentStart, rightBound + 1) - 1

                if maxValidEnd >= currentStart:
                    validSubstringCount += maxValidEnd - currentStart + 1

                loopStart(currentStart + 1)

            loopStart(leftBound)
            return validSubstringCount

        outputResults: List[int] = []

        def processQueries(index: int) -> None:
            if index == len(queries):
                return
            leftQueryBound, rightQueryBound = queries[index]
            outputResults.append(count_valid_substrings(leftQueryBound, rightQueryBound))
            processQueries(index + 1)

        processQueries(0)
        return outputResults