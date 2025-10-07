class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD_CONST = 10**9 + 7

        def computeProductAndSum(a: int, b: int, c: int, d: int) -> int:
            return ((a * b) + (c * d)) % MOD_CONST

        def init2DArray(rows: int, cols: int) -> list[list[int]]:
            def createRow(index: int, acc: list[int]) -> list[int]:
                if index > cols:
                    return acc
                else:
                    return createRow(index + 1, acc + [0])

            def buildRows(cur: int, acc: list[list[int]]) -> list[list[int]]:
                if cur > rows:
                    return acc
                else:
                    return buildRows(cur + 1, acc + [createRow(1, [])])

            return buildRows(1, [])

        arrayF = init2DArray(n + 1, x + 1)
        arrayF[0][0] = 1

        def outerLoopI(indexI: int) -> None:
            if indexI > n:
                return

            def innerLoopJ(indexJ: int) -> None:
                if indexJ > x:
                    return

                val1 = arrayF[indexI - 1][indexJ] if indexJ <= x else 0
                val2 = arrayF[indexI - 1][indexJ - 1] if indexJ - 1 >= 0 else 0
                mult1 = val1 * indexJ
                mult2 = val2 * (x - (indexJ - 1))
                combinedVal = (mult1 + mult2) % MOD_CONST

                arrayF[indexI][indexJ] = combinedVal

                innerLoopJ(indexJ + 1)

            innerLoopJ(1)
            outerLoopI(indexI + 1)

        outerLoopI(1)

        resultAccum = 0
        powerAcc = 1

        def loopJpower(indexJ: int) -> None:
            nonlocal resultAccum, powerAcc
            if indexJ > x:
                return

            powerAcc = (powerAcc * y) % MOD_CONST
            tempVal = arrayF[n][indexJ] * powerAcc
            resultAccum = (resultAccum + tempVal) % MOD_CONST

            loopJpower(indexJ + 1)

        loopJpower(1)

        return resultAccum