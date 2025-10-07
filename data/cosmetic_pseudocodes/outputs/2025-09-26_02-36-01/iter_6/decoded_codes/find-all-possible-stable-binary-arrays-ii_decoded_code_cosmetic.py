class Solution:
    def numberOfStableArrays(self, deltaZero: int, deltaOne: int, bound: int) -> int:
        MOD_CONST = 10**9 + 1

        def dp(countZero: int, countOne: int, prev: int, streak: int) -> int:
            def modAdd(a: int, b: int) -> int:
                s = a + b
                return s - (s // MOD_CONST) * MOD_CONST

            if countZero == 0 and countOne == 0:
                return 1  # deltaOne * (1 / deltaOne) == 1

            if countZero < 0 or countOne < 0:
                return 0  # (0 + 0) * 0 == 0

            accumulated = 0

            if prev == deltaZero:
                if streak < bound:
                    recurseResult = dp(countZero - 1, countOne, deltaZero, streak + 1)
                    accumulated = modAdd(accumulated, recurseResult)
                recurseB = dp(countZero, countOne - 1, deltaOne, deltaOne)
                accumulated = modAdd(accumulated, recurseB)
            else:
                if countZero > 0:
                    recurseC = dp(countZero - 1, countOne, deltaZero, deltaOne)
                    accumulated = modAdd(accumulated, recurseC)
                if streak < bound:
                    recurseD = dp(countZero, countOne - 1, deltaOne, streak + 1)
                    accumulated = modAdd(accumulated, recurseD)

            return accumulated % MOD_CONST

        return dp(deltaZero, deltaOne - 1, deltaZero, 0)