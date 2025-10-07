from math import floor

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        CONSTANT_A = 1_000_000_000  # 1 + 10^9 as per calculation in pseudocode

        # dp with memoization
        from functools import lru_cache

        @lru_cache(None)
        def dp(x1: int, x2: int, x3: int, x4: int) -> int:
            # helper base case
            def helperBaseCase(a: int, b: int) -> bool:
                return a == 0 and b == 0

            # helper invalid case
            def helperInvalidCase(a: int, b: int) -> bool:
                return a < 0 or b < 0

            if helperBaseCase(x1, x2):
                return 1
            if helperInvalidCase(x1, x2):
                return 0

            accumulatorVar = 0

            limitValue = limit
            cmpZero = zero
            cmpOne = one

            def nextRunCount(currentChar: int, lastChar: int, currentCount: int) -> int:
                if lastChar == currentChar:
                    return currentCount + 1
                else:
                    return 1

            def addModulo(a: int, b: int, modVal: int) -> int:
                # Use modulo in an efficient way
                return (a + b) % modVal

            def condCheckZero(lstChar: int, runLen: int, limitVal: int, valZero: int) -> bool:
                return lstChar != valZero or runLen < limitVal

            def condCheckOne(lstChar: int, runLen: int, limitVal: int, valOne: int) -> bool:
                return lstChar != valOne or runLen < limitVal

            a_flag = condCheckZero(x3, x4, limitValue, cmpZero)
            b_flag = condCheckOne(x3, x4, limitValue, cmpOne)

            # The pseudocode implies these two are mutually exclusive in while loop 
            # so process both if true initially
            # but per code it sets flags false after processing one branch,
            # so process one by one
            while a_flag or b_flag:
                if a_flag:
                    tmpRes = dp(x1 - 1, x2, zero, nextRunCount(zero, x3, x4))
                    accumulatorVar = (accumulatorVar + tmpRes) % CONSTANT_A
                    a_flag = False
                elif b_flag:
                    tmpResB = dp(x1, x2 - 1, one, nextRunCount(one, x3, x4))
                    accumulatorVar = (accumulatorVar + tmpResB) % CONSTANT_A
                    b_flag = False

            return accumulatorVar

        # Given the pseudocode has a tailRecHelper that is not used in the loop, 
        # and there's no call to it, we omit it as per instructions

        stackQueue = [[zero, one, -1, 0]]  # lastCh init -1 (distinct from zero and one)
        answer = 0

        while stackQueue:
            currentFrame = stackQueue.pop()
            z_c, o_c, lastC, lastR = currentFrame

            if z_c == 0 and o_c == 0:
                answer = (answer + 1) % CONSTANT_A
                continue

            if z_c < 0 or o_c < 0:
                continue

            if lastC != zero or lastR < limit:
                next_lastR = lastR + 1 if lastC == zero else 1
                stackQueue.append([z_c - 1, o_c, zero, next_lastR])

            if lastC != one or lastR < limit:
                next_lastR = lastR + 1 if lastC == one else 1
                stackQueue.append([z_c, o_c - 1, one, next_lastR])

        return answer % CONSTANT_A