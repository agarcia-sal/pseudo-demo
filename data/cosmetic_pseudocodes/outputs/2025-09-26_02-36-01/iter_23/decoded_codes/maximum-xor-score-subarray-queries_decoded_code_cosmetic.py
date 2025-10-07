from typing import List

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        W = len(nums)

        def buildFX(nums: List[int]) -> List[List[int]]:
            def recurF(i: int) -> List[List[int]]:
                if i < 0:
                    return [[0] * W for _ in range(W)]
                else:
                    partialF = recurF(i - 1)
                    matrixF = partialF
                    p = i
                    q = i
                    while q < W:
                        if q == p:
                            matrixF[p][q] = nums[p]
                        else:
                            left = matrixF[p][q - 1]
                            down = matrixF[p + 1][q]
                            matrixF[p][q] = left ^ down
                        q += 1
                    return matrixF
            return recurF(W - 1)

        def buildTableY(f: List[List[int]]) -> List[List[int]]:
            def recurY(row: int, col: int) -> List[List[int]]:
                if row < 0:
                    return [[0] * W for _ in range(W)]
                else:
                    prevMatrix = recurY(row - 1, col)
                    currMatrix = prevMatrix
                    iX = row
                    jX = row
                    while jX < W:
                        val1 = f[iX][jX]
                        val2 = currMatrix[iX][jX - 1] if jX > iX else 0
                        val3 = currMatrix[iX + 1][jX] if iX + 1 < W else 0
                        candidates = [val1, val2, val3]
                        maxVal = max(candidates)
                        currMatrix[iX][jX] = maxVal
                        jX += 1
                    return currMatrix
            return recurY(W - 1, 0)

        tmpF = buildFX(nums)
        tmpG = buildTableY(tmpF)
        resultList = []

        def processQueries(qList: List[List[int]], idx: int):
            if idx == len(qList):
                return
            else:
                li, ri = qList[idx]
                resultList.append(tmpG[li][ri])
                processQueries(qList, idx + 1)

        processQueries(queries, 0)

        return resultList