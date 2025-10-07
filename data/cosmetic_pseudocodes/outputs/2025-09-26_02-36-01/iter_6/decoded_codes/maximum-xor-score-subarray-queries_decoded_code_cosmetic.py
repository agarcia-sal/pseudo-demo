from typing import List

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        count = len(nums)

        def bitwiseXor(a: int, b: int) -> int:
            return a ^ b

        matrixF = [[0] * count for _ in range(count)]
        matrixG = [[0] * count for _ in range(count)]

        def procFill(posIdx: int) -> None:
            if posIdx >= count:
                return
            matrixF[posIdx][posIdx] = nums[posIdx]
            matrixG[posIdx][posIdx] = nums[posIdx]

            def fillLoop(currentPos: int) -> None:
                if currentPos >= count:
                    return

                leftXorValue = matrixF[posIdx][currentPos - 1]
                rightXorValue = matrixF[posIdx + 1][currentPos]
                xorCalc = bitwiseXor(leftXorValue, rightXorValue)
                matrixF[posIdx][currentPos] = xorCalc

                leftMax = matrixG[posIdx][currentPos]
                maxLeft = matrixG[posIdx][currentPos - 1]
                maxRight = matrixG[posIdx + 1][currentPos]

                computeMax1 = leftMax
                if maxLeft > computeMax1:
                    computeMax1 = maxLeft
                if maxRight > computeMax1:
                    computeMax1 = maxRight
                matrixG[posIdx][currentPos] = computeMax1

                fillLoop(currentPos + 1)

            fillLoop(posIdx + 1)
            procFill(posIdx + 1)

        procFill(0)

        resultAccumulator = []
        for lowerBound, upperBound in queries:
            resultAccumulator.append(matrixG[lowerBound][upperBound])

        return resultAccumulator