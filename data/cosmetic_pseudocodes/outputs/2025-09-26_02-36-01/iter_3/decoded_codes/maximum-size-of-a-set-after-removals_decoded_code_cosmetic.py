from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        lengthNums = len(nums1)
        countNums = lengthNums // 2

        distinctNums1 = set(nums1)
        distinctNums2 = set(nums2)

        sharedNums = distinctNums1 & distinctNums2

        exclusiveNums1 = distinctNums1 - sharedNums
        exclusiveNums2 = distinctNums2 - sharedNums

        maxTake1 = min(countNums, len(exclusiveNums1))
        maxTake2 = min(countNums, len(exclusiveNums2))

        left1 = countNums - maxTake1
        if left1 < 0:
            left1 = 0
        left2 = countNums - maxTake2
        if left2 < 0:
            left2 = 0

        takeFromShared = left1 + left2
        if takeFromShared > len(sharedNums):
            takeFromShared = len(sharedNums)

        return maxTake1 + maxTake2 + takeFromShared