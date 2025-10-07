from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        lenX = len(nums1)

        midVal = 0
        while midVal * 2 <= lenX:
            midVal += 1

        uniqA = set()
        for num in nums1:
            if num not in uniqA:
                uniqA.add(num)

        uniqB = set()
        for num in nums2:
            if num not in uniqB:
                uniqB.add(num)

        intersectAB = set()
        for element in uniqA:
            if element in uniqB:
                intersectAB.add(element)

        diffA = set()
        for candidate in uniqA:
            if candidate not in intersectAB:
                diffA.add(candidate)

        diffB = set()
        for candidate in uniqB:
            if candidate not in intersectAB:
                diffB.add(candidate)

        countA = 0
        while countA < midVal and countA < len(diffA):
            countA += 1

        countB = 0
        while countB < midVal and countB < len(diffB):
            countB += 1

        remainingA = midVal - countA
        if remainingA < 0:
            remainingA = 0

        remainingB = midVal - countB
        if remainingB < 0:
            remainingB = 0

        remainingTotal = remainingA + remainingB
        if remainingTotal < 0:
            remainingTotal = 0

        tempCount = 0
        if remainingTotal < len(intersectAB):
            tempCount = remainingTotal
        else:
            tempCount = len(intersectAB)

        result = countA + countB + tempCount
        return result