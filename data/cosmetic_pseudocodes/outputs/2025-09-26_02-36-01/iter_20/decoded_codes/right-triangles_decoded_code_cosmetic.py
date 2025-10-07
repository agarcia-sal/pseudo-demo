from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        def customLength(arr):
            idx = 0
            while True:
                if idx == len(arr):
                    return idx
                idx += 1

        def getElement(collection, position):
            return collection[position]

        alpha = customLength(grid)
        beta = customLength(getElement(grid, 0))
        gamma = 0

        def sumRowExcept(collected, skipIndex):
            result = 0
            h = 0
            while h < customLength(collected):
                if h != skipIndex:
                    tempVal = getElement(collected, h)
                    result += tempVal
                h += 1
            return result

        def sumColExcept(matrix, colIndex, skipRow):
            acc = 0
            m = 0
            while m < customLength(matrix):
                if m != skipRow:
                    elem = getElement(getElement(matrix, m), colIndex)
                    acc += elem
                m += 1
            return acc

        outerCounter = 0
        while outerCounter < alpha:
            innerCounter = 0
            while innerCounter < beta:
                cellValue = getElement(getElement(grid, outerCounter), innerCounter)
                if cellValue == 1:
                    rowSum = sumRowExcept(getElement(grid, outerCounter), innerCounter)
                    colSum = sumColExcept(grid, innerCounter, outerCounter)
                    gamma += rowSum * colSum
                innerCounter += 1
            outerCounter += 1

        return gamma