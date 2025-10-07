from math import inf
from typing import List

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        onesIdx = []
        posCounter = 0
        while posCounter < len(nums):
            if nums[posCounter] == 1:
                onesIdx.append(posCounter)
            posCounter += 1

        if len(onesIdx) == 0:
            return k * 2

        count = len(onesIdx)
        prefix = [0] * (count + 1)

        indexer = 0
        while indexer < count:
            prefix[indexer + 1] = prefix[indexer] + onesIdx[indexer]
            indexer += 1

        def cost(start: int, end: int) -> int:
            center = (start + end) // 2
            medianVal = onesIdx[center]
            totalCost = 0
            l = start
            while l < center:
                diff1 = medianVal - onesIdx[l]
                diff2 = center - l
                totalCost += (diff1 - diff2)
                l += 1
            r = center + 1
            while r <= end:
                diff3 = onesIdx[r] - medianVal
                diff4 = r - center
                totalCost += (diff3 - diff4)
                r += 1
            return totalCost

        minimalMoves = inf
        s = 0
        while s <= count - k:
            e = s + k - 1
            currCost = cost(s, e)

            if k % 2 == 1:
                mid = (s + e) // 2
                med = onesIdx[mid]
                # Carefully handle index med-1, ensure in bounds
                left_val = onesIdx[mid - 1] if mid - 1 >= 0 else 0
                neededChanges = (e - mid) - (med - left_val)
            else:
                leftMid = (s + e) // 2
                rightMid = leftMid + 1
                leftMed = onesIdx[leftMid]
                rightMed = onesIdx[rightMid]
                neededChanges = (rightMid - leftMid - 1) - (rightMed - leftMed - 1)

            if neededChanges > maxChanges:
                currCost += (neededChanges - maxChanges)

            if currCost < minimalMoves:
                minimalMoves = currCost

            s += 1

        return minimalMoves