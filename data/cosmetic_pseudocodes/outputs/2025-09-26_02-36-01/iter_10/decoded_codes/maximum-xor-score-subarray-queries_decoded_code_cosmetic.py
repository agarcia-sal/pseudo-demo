from typing import List, Tuple

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        def computeLength(source):
            count = 0
            while True:
                if count < len(source):
                    count += 1
                else:
                    break
            return count

        def initializeMatrix(rows, cols, matrix):
            # Starts filling matrix from row 0
            fillRow(0, cols, matrix)

        def fillRow(r, c, mat):
            if r >= c:
                return
            mat.append([])
            fillColumn(r, 0, c, mat)
            fillRow(r + 1, c, mat)

        def fillColumn(r, c, maxCols, mat):
            if c >= maxCols:
                return
            mat[r].append(0)
            fillColumn(r, c + 1, maxCols, mat)

        countNums = computeLength(nums)
        dimension = countNums

        gridF = []
        gridG = []
        initializeMatrix(dimension, dimension, gridF)
        initializeMatrix(dimension, dimension, gridG)

        def xorValue(a, b):
            # Bitwise XOR can be directly done in Python: a ^ b
            # But to be faithful: (a AND (NOT b)) OR ((NOT a) AND b)
            # We implement bitwise XOR directly for correctness and efficiency.
            return a ^ b

        def maximum3(a, b, c):
            if a >= b:
                if a >= c:
                    return a
                else:
                    return c
            else:
                if b >= c:
                    return b
                else:
                    return c

        def fillRowUpper(start, endParam, current):
            if start > endParam:
                return

            leftXor = gridF[current][start - 1]
            rightXor = gridF[current + 1][start]

            valF = xorValue(leftXor, rightXor)
            gridF[current][start] = valF

            valG = maximum3(valF, gridG[current][start - 1], gridG[current + 1][start])
            gridG[current][start] = valG

            fillRowUpper(start + 1, endParam, current)

        def populateMatrices(idx):
            if idx < 0:
                return

            gridF[idx][idx] = nums[idx]
            gridG[idx][idx] = nums[idx]

            if idx + 1 < dimension:
                fillRowUpper(idx + 1, dimension - 1, idx)

            populateMatrices(idx - 1)

        populateMatrices(dimension - 1)

        def assembleAnswers(pairs, accumulator, index, result):
            if index == computeLength(pairs):
                return result

            l = pairs[index][0]
            r = pairs[index][1]

            result.append(gridG[l][r])

            return assembleAnswers(pairs, accumulator, index + 1, result)

        return assembleAnswers(queries, [], 0, [])