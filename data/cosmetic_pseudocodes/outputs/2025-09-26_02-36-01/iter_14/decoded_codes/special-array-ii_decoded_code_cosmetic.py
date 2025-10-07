from typing import List, Tuple

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        auxiliaryList = [num % 2 for num in nums]

        cumulativeArray = [0] * len(nums)
        for position in range(1, len(nums)):
            if auxiliaryList[position] == auxiliaryList[position - 1]:
                cumulativeArray[position] = cumulativeArray[position - 1] + 1
            else:
                cumulativeArray[position] = cumulativeArray[position - 1]

        outputAccumulator = []
        for startPoint, endPoint in queries:
            if startPoint == endPoint:
                outputAccumulator.append(True)
            else:
                baseValue = cumulativeArray[startPoint] if startPoint > 0 else 0
                deltaValue = cumulativeArray[endPoint] - baseValue
                outputAccumulator.append(deltaValue == 0)

        return outputAccumulator