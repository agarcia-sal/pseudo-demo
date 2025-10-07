from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        lengthA = len(nums)
        lengthB = len(pattern)
        totalMatches = 0
        indexMain = 0
        # Loop while the subarray can be formed with lengthB elements
        while indexMain <= lengthA - lengthB:
            isValid = True
            if self.verifySegment(indexMain, lengthB, nums, pattern):
                totalMatches += 1
            indexMain += 1
        return totalMatches

    def verifySegment(self, startPos: int, segmentLength: int, arrNums: List[int], arrPattern: List[int]) -> bool:
        offset = 0
        # Check pairs within the segment as per pattern values
        while offset < segmentLength - 1:
            currentPatternValue = arrPattern[offset]
            firstNum = arrNums[startPos + offset]
            secondNum = arrNums[startPos + offset + 1]

            if currentPatternValue == 1:
                if not (firstNum < secondNum):
                    return False
            elif currentPatternValue == 0:
                if firstNum == secondNum:
                    return False
            elif currentPatternValue == -1:
                if not (firstNum > secondNum):
                    return False
            else:
                # If pattern has invalid values, treat as fail-safe to False
                return False
            offset += 1
        return True