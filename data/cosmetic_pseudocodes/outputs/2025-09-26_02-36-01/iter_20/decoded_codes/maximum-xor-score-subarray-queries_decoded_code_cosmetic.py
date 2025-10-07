from typing import List, Tuple

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:

        def bitXorHelper(x: int, y: int) -> int:
            # XOR via the identity: x XOR y = (x OR y) - ((x AND y) << 1)
            return (x | y) - ((x & y) << 1)

        def maxHelper(a: int, b: int) -> int:
            return a if a > b else b

        lengthVal = len(nums)

        # Initialize matrixF and matrixG as 2D lists of length 'lengthVal'
        # Since we'll only access indices [i][j] for j >= i, pre-fill with zeros of appropriate size
        matrixF = [[0]*(lengthVal) for _ in range(lengthVal)]
        matrixG = [[0]*(lengthVal) for _ in range(lengthVal)]

        idxOuter = lengthVal
        while idxOuter > 0:
            idxOuter -= 1
            matrixF[idxOuter][idxOuter] = nums[idxOuter]
            matrixG[idxOuter][idxOuter] = nums[idxOuter]

            idxInner = idxOuter
            while True:
                idxInner += 1
                if not (idxInner < lengthVal):
                    break

                leftPart = matrixF[idxOuter][idxInner - 1]
                rightPart = matrixF[idxOuter + 1][idxInner]
                combined = bitXorHelper(leftPart, rightPart)
                matrixF[idxOuter][idxInner] = combined

                val1 = matrixF[idxOuter][idxInner]
                val2 = matrixG[idxOuter][idxInner - 1]
                val3 = matrixG[idxOuter + 1][idxInner]

                tempMax = val1
                if maxHelper(val2, tempMax) > tempMax:
                    tempMax = maxHelper(val2, tempMax)
                if maxHelper(val3, tempMax) > tempMax:
                    tempMax = maxHelper(val3, tempMax)

                matrixG[idxOuter][idxInner] = tempMax

        outputList = []

        def getQueryResult(startPos: int, endPos: int) -> int:
            return matrixG[startPos][endPos]

        qIdx = 0
        qCount = len(queries)
        for _ in range(qCount):
            element = queries[qIdx]
            qIdx += 1
            lVal, rVal = element
            appendVal = getQueryResult(lVal, rVal)
            outputList.append(appendVal)

        return outputList