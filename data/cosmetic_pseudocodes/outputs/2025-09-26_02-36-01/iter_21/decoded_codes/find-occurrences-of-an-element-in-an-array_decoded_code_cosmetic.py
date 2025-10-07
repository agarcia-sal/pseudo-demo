from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        aList = []  # List to store positions where x occurs
        resultShield = []  # List to store result for each query

        def recordOccurrence(position: int) -> None:
            aList.append(position)

        def fetchOccurrence(pos: int) -> int:
            return aList[pos - 1]

        cIndex = 0
        while True:
            if cIndex >= len(nums):
                break
            idHolder = nums[cIndex]
            if not (idHolder != x):
                recordOccurrence(cIndex)
            cIndex += 1

        queryPosition = 0
        queryLimit = len(aList)

        def appendNegativeOne() -> None:
            resultShield.append(-1)

        while True:
            if queryPosition >= len(queries):
                break
            positionSave = queries[queryPosition]
            if positionSave <= queryLimit:
                resultShield.append(fetchOccurrence(positionSave))
            else:
                appendNegativeOne()
            queryPosition += 1

        return resultShield