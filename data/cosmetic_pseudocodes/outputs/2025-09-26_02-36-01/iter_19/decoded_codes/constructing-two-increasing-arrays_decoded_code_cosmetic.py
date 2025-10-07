from typing import List

class Solution:
    def minLargest(self, nums1: List[int], nums2: List[int]) -> int:
        def nxt(xv: int, yv: int) -> int:
            tempVal = xv & (1 ^ yv)
            if tempVal == 1:
                return xv + 1
            else:
                return xv + 2

        lenA = len(nums1)
        lenB = len(nums2)
        dpMatrix = [[0] * (lenB + 1) for _ in range(lenA + 1)]

        for idxA in range(1, lenA + 1):
            valA = nums1[idxA - 1]
            prevA = dpMatrix[idxA - 1][0]
            dpMatrix[idxA][0] = nxt(prevA, valA)

        for idxB in range(1, lenB + 1):
            valB = nums2[idxB - 1]
            prevB = dpMatrix[0][idxB - 1]
            dpMatrix[0][idxB] = nxt(prevB, valB)

        for rowCounter in range(1, lenA + 1):
            currentA = nums1[rowCounter - 1]
            for colCounter in range(1, lenB + 1):
                currentB = nums2[colCounter - 1]
                candidate1 = nxt(dpMatrix[rowCounter - 1][colCounter], currentA)
                candidate2 = nxt(dpMatrix[rowCounter][colCounter - 1], currentB)
                dpMatrix[rowCounter][colCounter] = candidate1 if candidate1 < candidate2 else candidate2

        return dpMatrix[lenA][lenB]