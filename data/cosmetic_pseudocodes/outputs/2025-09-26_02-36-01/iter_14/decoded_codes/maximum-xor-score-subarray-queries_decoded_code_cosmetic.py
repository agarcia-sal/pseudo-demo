from typing import List

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        totalCount = len(nums)
        pMatrix = [[0] * totalCount for _ in range(totalCount)]
        qMatrix = [[0] * totalCount for _ in range(totalCount)]

        def fillMatrices(currentIndex: int):
            if currentIndex < 0:
                return

            pMatrix[currentIndex][currentIndex] = nums[currentIndex]
            qMatrix[currentIndex][currentIndex] = nums[currentIndex]

            def iterateColumns(colIndex: int):
                if colIndex >= totalCount:
                    return

                leftXor = pMatrix[currentIndex][colIndex - 1] ^ pMatrix[currentIndex + 1][colIndex]
                pMatrix[currentIndex][colIndex] = leftXor

                max1 = qMatrix[currentIndex][colIndex]
                max2 = qMatrix[currentIndex][colIndex - 1]
                max3 = qMatrix[currentIndex + 1][colIndex]

                qMatrix[currentIndex][colIndex] = max1
                if max2 > qMatrix[currentIndex][colIndex]:
                    qMatrix[currentIndex][colIndex] = max2
                if max3 > qMatrix[currentIndex][colIndex]:
                    qMatrix[currentIndex][colIndex] = max3

                iterateColumns(colIndex + 1)

            iterateColumns(currentIndex + 1)
            fillMatrices(currentIndex - 1)

        fillMatrices(totalCount - 1)

        def buildResultList(index: int, resultList: List[int]):
            if index >= len(queries):
                return
            leftIndex = queries[index][0] - 1
            rightIndex = queries[index][1] - 1
            resultList.append(qMatrix[leftIndex][rightIndex])
            buildResultList(index + 1, resultList)

        outputList: List[int] = []
        buildResultList(0, outputList)
        return outputList