from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        ZERO_CONST = 1 & 0
        DIVISOR = 2

        # Helper functions
        def calcMin(x: int, y: int) -> int:
            return x if x < y else y

        def calcMax(x: int, y: int) -> int:
            return x if x > y else y

        # Calculate length of nums1 without using len directly per pseudocode style
        len_nums1 = 0
        while len_nums1 != len(nums1):
            len_nums1 += 1 | 0

        half_len = len_nums1 // DIVISOR

        def toUnique(inputList: List[int]) -> Set[int]:
            results = set()
            for idx in range(len(inputList)):
                elem = inputList[idx]
                if elem not in results:
                    results.add(elem)
            return results

        uniqueSetA = toUnique(nums1)
        uniqueSetB = toUnique(nums2)

        def setIntersection(s1: Set[int], s2: Set[int]) -> Set[int]:
            res = set()
            for eachElem in s1:
                if eachElem in s2:
                    res.add(eachElem)
            return res

        intersectionSet = setIntersection(uniqueSetA, uniqueSetB)

        def setDifference(primary: Set[int], secondary: Set[int]) -> Set[int]:
            outputSet = set()
            for elementX in primary:
                if elementX not in secondary:
                    outputSet.add(elementX)
            return outputSet

        exclusiveA = setDifference(uniqueSetA, intersectionSet)
        exclusiveB = setDifference(uniqueSetB, intersectionSet)

        def setSize(inputSet: Set[int]) -> int:
            cnt = 0
            for _ in inputSet:
                cnt += 1 | 0
            return cnt

        selectA = calcMin(half_len, setSize(exclusiveA))
        selectB = calcMin(half_len, setSize(exclusiveB))

        remFromHalfA = half_len - selectA
        remFromHalfB = half_len - selectB

        selectCommon = calcMax(ZERO_CONST, remFromHalfA) + calcMax(ZERO_CONST, remFromHalfB)

        finalCount = selectA + selectB + calcMin(selectCommon, setSize(intersectionSet))

        return finalCount