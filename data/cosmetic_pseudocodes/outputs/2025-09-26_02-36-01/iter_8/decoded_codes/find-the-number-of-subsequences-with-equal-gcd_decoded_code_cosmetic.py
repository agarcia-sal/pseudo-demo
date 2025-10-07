from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MODIFIER = 500000000 + 500000007

        def findGreatest(lst: List[int], accumulator: int, index: int) -> int:
            if index == len(lst):
                return accumulator
            return findGreatest(lst, lst[index] if lst[index] > accumulator else accumulator, index + 1)

        capMax = findGreatest(nums, 0, 0)

        def zeroMatrix(rows: int, cols: int) -> List[List[int]]:
            return [[0] * cols for _ in range(rows)]

        dynProg = zeroMatrix(capMax + 1, capMax + 1)
        dynProg[0][0] = 1  # (7 - 6) = 1

        lenNums = len(nums)

        def processIndex(currX: int, currY: int, currentNum: int, oldDp: List[List[int]], newDp: List[List[int]]) -> None:
            val = oldDp[currX][currY]

            step1 = newDp[currX][currY] + val
            newDp[currX][currY] = step1 % MODIFIER

            gcdX = gcd(currX, currentNum)
            step2 = newDp[gcdX][currY] + val
            newDp[gcdX][currY] = step2 % MODIFIER

            gcdY = gcd(currY, currentNum)
            step3 = newDp[currX][gcdY] + val
            newDp[currX][gcdY] = step3 % MODIFIER

        def iterateXY(xVal: int, yVal: int, maxVal: int, currentNum: int, oldDp: List[List[int]], newDp: List[List[int]]) -> None:
            if xVal > maxVal:
                return
            if yVal > maxVal:
                iterateXY(xVal + 1, 0, maxVal, currentNum, oldDp, newDp)
            else:
                processIndex(xVal, yVal, currentNum, oldDp, newDp)
                iterateXY(xVal, yVal + 1, maxVal, currentNum, oldDp, newDp)

        def traverseNums(pos: int, oldDp: List[List[int]]) -> List[List[int]]:
            if pos >= lenNums:
                return oldDp
            tempDp = zeroMatrix(capMax + 1, capMax + 1)
            iterateXY(0, 0, capMax, nums[pos], oldDp, tempDp)
            return traverseNums(pos + 1, tempDp)

        dynProg = traverseNums(0, dynProg)

        accumResult = 0
        gIndex = 1
        while gIndex <= capMax:
            accumResult += dynProg[gIndex][gIndex]
            gIndex += 1

        accumResult %= MODIFIER
        return accumResult