from typing import List, Tuple

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        lengthVar = len(nums)

        def helperCreateMatrix(size: int) -> List[List[int]]:
            return [[0]*size for _ in range(size)]

        firstMatrix = helperCreateMatrix(lengthVar)
        secondMatrix = helperCreateMatrix(lengthVar)

        iVar = lengthVar - 1
        while iVar >= 0:
            firstMatrix[iVar][iVar] = nums[iVar]
            secondMatrix[iVar][iVar] = nums[iVar]

            jVar = iVar + 1
            while jVar < lengthVar:
                tempXor1 = firstMatrix[iVar][jVar - 1]
                tempXor2 = firstMatrix[iVar + 1][jVar]
                firstMatrix[iVar][jVar] = tempXor1 ^ tempXor2

                val1 = firstMatrix[iVar][jVar]
                val2 = secondMatrix[iVar][jVar - 1]
                val3 = secondMatrix[iVar + 1][jVar]

                if val1 >= val2:
                    if val1 >= val3:
                        secondMatrix[iVar][jVar] = val1
                    else:
                        secondMatrix[iVar][jVar] = val3
                else:
                    if val2 >= val3:
                        secondMatrix[iVar][jVar] = val2
                    else:
                        secondMatrix[iVar][jVar] = val3

                jVar += 1
            iVar -= 1

        def makeResults(queryList: List[Tuple[int, int]]) -> List[int]:
            outputList = []
            for startIdx, endIdx in queryList:
                outputList.append(secondMatrix[startIdx][endIdx])
            return outputList

        return makeResults(queries)