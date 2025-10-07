from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        lengthNums1 = len(nums1)
        halfLength = lengthNums1 // 2

        setA = set(nums1)
        setB = set(nums2)

        intersectionSet = setA & setB

        exclusiveA = setA - intersectionSet
        exclusiveB = setB - intersectionSet

        pickA = halfLength if halfLength < len(exclusiveA) else len(exclusiveA)
        pickB = halfLength if halfLength < len(exclusiveB) else len(exclusiveB)

        remainA = halfLength - pickA
        remainB = halfLength - pickB

        remainA = remainA if remainA > 0 else 0
        remainB = remainB if remainB > 0 else 0

        pickCommon = remainA + remainB
        if pickCommon > len(intersectionSet):
            pickCommon = len(intersectionSet)

        totalCount = pickA + pickB + pickCommon
        return totalCount