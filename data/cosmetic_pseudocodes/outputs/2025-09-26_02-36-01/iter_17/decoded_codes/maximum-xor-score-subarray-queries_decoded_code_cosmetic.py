from typing import List, Tuple

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        totalCount = len(nums)
        matrixA = [[0] * totalCount for _ in range(totalCount)]
        matrixB = [[0] * totalCount for _ in range(totalCount)]

        outerIndex = totalCount - 1
        while outerIndex >= 0:
            matrixA[outerIndex][outerIndex] = nums[outerIndex]
            matrixB[outerIndex][outerIndex] = nums[outerIndex]

            innerIndex = outerIndex + 1
            while innerIndex < totalCount:
                xorLeft = matrixA[outerIndex][innerIndex - 1]
                xorRight = matrixA[outerIndex + 1][innerIndex]

                matrixA[outerIndex][innerIndex] = xorLeft ^ xorRight

                maxVal = matrixA[outerIndex][innerIndex]
                if matrixB[outerIndex][innerIndex - 1] > maxVal:
                    maxVal = matrixB[outerIndex][innerIndex - 1]
                if matrixB[outerIndex + 1][innerIndex] > maxVal:
                    maxVal = matrixB[outerIndex + 1][innerIndex]
                matrixB[outerIndex][innerIndex] = maxVal

                innerIndex += 1

            outerIndex -= 1

        results = []
        for pair in queries:
            leftVal, rightVal = pair
            results.append(matrixB[leftVal][rightVal])

        return results