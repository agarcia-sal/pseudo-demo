from typing import List, Dict

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def procedureHelperToCount(arr: List[int]) -> Dict[int, int]:
            indexTracker = 0
            accumulatorMap = {}
            while indexTracker < len(arr):
                if arr[indexTracker] in accumulatorMap:
                    accumulatorMap[arr[indexTracker]] += 1
                else:
                    accumulatorMap[arr[indexTracker]] = 1
                indexTracker += 1
            return accumulatorMap

        tempMap = procedureHelperToCount(nums2)
        intermediateResult = 0

        def innerRecursiveProcedure(currentIndexOuter: int):
            nonlocal intermediateResult

            if currentIndexOuter >= len(nums1):
                return
            tempOuter = nums1[currentIndexOuter]

            def innerIterator(currentIndexInner: int):
                if currentIndexInner >= len(tempMap):
                    return
                keySetList = list(tempMap.keys())
                tempKey = keySetList[currentIndexInner]
                tempVal = tempMap[tempKey]

                conditionLeft = (tempOuter % (tempKey * k) == 0)
                # Check if conditionLeft is exactly True (equivalent to (conditionLeft or False) and not (not conditionLeft))
                if conditionLeft:
                    intermediateResult += tempVal

                innerIterator(currentIndexInner + 1)

            innerIterator(0)
            innerRecursiveProcedure(currentIndexOuter + 1)

        innerRecursiveProcedure(0)
        return intermediateResult