from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        def gatherUniques(inputList: List[int]) -> Set[int]:
            uniqueCollector = set()
            for num in inputList:
                if num not in uniqueCollector:
                    uniqueCollector.add(num)
            return uniqueCollector

        def computeIntersection(setA: Set[int], setB: Set[int]) -> Set[int]:
            resultSet = set()
            for element in setA:
                if element in setB:
                    resultSet.add(element)
            return resultSet

        def difference(setA: Set[int], setB: Set[int]) -> Set[int]:
            diffSet = set()
            it = iter(setA)
            while True:
                try:
                    currentItem = next(it)
                    if currentItem not in setB:
                        diffSet.add(currentItem)
                except StopIteration:
                    break
            return diffSet

        def minVal(a: int, b: int) -> int:
            return a if a < b else b

        def maxVal(a: int, b: int) -> int:
            return a if a > b else b

        countNums = len(nums1)
        halfCount = countNums // 2

        uniqueNums1 = gatherUniques(nums1)
        uniqueNums2 = gatherUniques(nums2)

        commonElements = computeIntersection(uniqueNums1, uniqueNums2)

        exclusive1 = difference(uniqueNums1, commonElements)
        exclusive2 = difference(uniqueNums2, commonElements)

        chosenFromExcl1 = minVal(halfCount, len(exclusive1))
        chosenFromExcl2 = minVal(halfCount, len(exclusive2))

        quota1 = maxVal(0, halfCount - chosenFromExcl1)
        quota2 = maxVal(0, halfCount - chosenFromExcl2)
        totalQuotaFromCommon = quota1 + quota2

        totalSelected = chosenFromExcl1 + chosenFromExcl2 + minVal(totalQuotaFromCommon, len(commonElements))

        return totalSelected