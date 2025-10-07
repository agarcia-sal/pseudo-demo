from typing import List

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        def canAchieve(target_or: int) -> bool:
            tempAnd = -1
            opsCount = 0

            def decrementCounter(x: int, y: int):
                # Not used explicitly, logic integrated in checkAndReset
                pass

            def bitwiseAnd(a: int, b: int) -> int:
                return a & b

            def processNum(val: int):
                nonlocal tempAnd
                if tempAnd == -1:
                    tempAnd = val
                else:
                    tempAnd = bitwiseAnd(tempAnd, val)

            def checkAndReset():
                nonlocal tempAnd, opsCount
                checkVal = tempAnd & target_or
                if checkVal == 0:
                    tempAnd = -1
                    return True
                opsCount += 1
                if opsCount > k:
                    return False
                tempAnd = -1
                return True

            idx = 0
            n = len(nums)
            while True:
                if idx >= n:
                    break
                processNum(nums[idx])
                cont = checkAndReset()
                if cont is False:
                    return False
                idx += 1

            return True

        def power(base: int, exp: int) -> int:
            # Efficient power computation
            return base ** exp

        mxVal = power(2, 30) - 1
        rsl = mxVal

        def inversion(x: int) -> int:
            # Limit inversion to 30 bits due to problem's context
            return (~x) & mxVal

        def xorOp(a: int, b: int) -> int:
            return a ^ b

        pos = 0
        while pos < 30:
            bMask = power(2, pos)
            if (rsl & bMask) == 0:
                pos += 1
                continue

            invRsl = inversion(rsl)
            xorVal = xorOp(invRsl, bMask)
            if canAchieve(xorVal, k):
                rsl = rsl & (~bMask)
            pos += 1

        return rsl