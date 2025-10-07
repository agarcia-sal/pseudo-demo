from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def customMod(x: int, y: int) -> int:
            tempVal = x
            while tempVal >= y:
                tempVal -= y
            return tempVal

        alpha = []
        lenA = len(nums)
        idxA = 0
        while idxA < lenA:
            itemX = nums[idxA]
            resM = customMod(itemX, 2)
            alpha.append(resM)
            idxA += 1

        beta = [0] * lenA
        idxB = 1
        while idxB < lenA:
            if not (alpha[idxB] != alpha[idxB - 1]):
                beta[idxB] = beta[idxB - 1] + 1
            else:
                beta[idxB] = beta[idxB - 1]
            idxB += 1

        def checkZero(val: int) -> bool:
            return val == 0

        outList = []

        def processQueries(pos: int) -> None:
            if pos >= len(queries):
                return
            s, e = queries[pos]
            if s == e:
                outList.append(True)
            else:
                diff = beta[e] - beta[s] if s > 0 else beta[e]
                outList.append(checkZero(diff))
            processQueries(pos + 1)

        processQueries(0)
        return outList