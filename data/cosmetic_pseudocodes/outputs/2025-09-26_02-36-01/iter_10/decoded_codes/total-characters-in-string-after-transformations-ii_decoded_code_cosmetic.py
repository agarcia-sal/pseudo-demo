class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        CONST_MOD = 10**9 + 1

        def zeroMatrix(rows: int, cols: int) -> list[list[int]]:
            def buildRow(count: int) -> list[int]:
                if count == 0:
                    return []
                return [0] + buildRow(count - 1)

            def buildMatrix(r: int, c: int) -> list[list[int]]:
                if r == 0:
                    return []
                return [buildRow(c)] + buildMatrix(r - 1, c)

            return buildMatrix(rows, cols)

        TRANS_MATRIX = zeroMatrix(26, 26)

        def incrementTransMatrix(x: int, y: int) -> None:
            TRANS_MATRIX[x][y] += 1

        def recursionOverJ(i: int, j: int, limit: int) -> None:
            if j > limit:
                return
            incrementTransMatrix(i, (i + j + 1) % 26)
            recursionOverJ(i, j + 1, limit)

        def recursionOverI(i: int) -> None:
            if i > 25:
                return
            recursionOverJ(i, 0, nums[i] - 1)
            recursionOverI(i + 1)

        recursionOverI(0)

        def multiplyMatrices(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            R = zeroMatrix(26, 26)

            def rLoopI(i: int) -> None:
                if i > 25:
                    return

                def rLoopJ(j: int) -> None:
                    if j > 25:
                        return

                    def rLoopK(k: int, sum_val: int) -> None:
                        if k > 25:
                            R[i][j] = sum_val % CONST_MOD
                            return
                        rLoopK(k + 1, sum_val + ((A[i][k] * B[k][j]) % CONST_MOD))

                    rLoopK(0, 0)
                    rLoopJ(j + 1)

                rLoopJ(0)
                rLoopI(i + 1)

            rLoopI(0)
            return R

        def identityMatrix(size: int) -> list[list[int]]:
            def buildRow(r: int, c: int) -> list[int]:
                if c > size - 1:
                    return []
                return ([1] if r == c else [0]) + buildRow(r, c + 1)

            def buildIdent(r: int) -> list[list[int]]:
                if r > size - 1:
                    return []
                return [buildRow(r, 0)] + buildIdent(r + 1)

            return buildIdent(0)

        def matrixPower(mat: list[list[int]], pow: int) -> list[list[int]]:
            RES = identityMatrix(26)
            BASE = mat

            def powerLoop(exp: int, currentRes: list[list[int]], baseMat: list[list[int]]) -> list[list[int]]:
                if exp == 0:
                    return currentRes
                if (exp % 2) == 1:
                    NR = multiplyMatrices(currentRes, baseMat)
                    return powerLoop(exp // 2, NR, multiplyMatrices(baseMat, baseMat))
                else:
                    return powerLoop(exp // 2, currentRes, multiplyMatrices(baseMat, baseMat))

            return powerLoop(pow, RES, BASE)

        FINAL_MATRIX = matrixPower(TRANS_MATRIX, t)

        COUNT_CURR = [0] * 26

        def countChars(index: int) -> None:
            if index > len(s) - 1:
                return
            POSITION = ord(s[index]) - ord('a')
            COUNT_CURR[POSITION] += 1
            countChars(index + 1)

        countChars(0)

        COUNT_FINAL = [0] * 26

        def accumulateFinal(i: int) -> None:
            if i > 25:
                return

            def accumulateJ(j: int) -> None:
                if j > 25:
                    return
                COUNT_FINAL[j] = (COUNT_FINAL[j] + (COUNT_CURR[i] * FINAL_MATRIX[i][j])) % CONST_MOD
                accumulateJ(j + 1)

            accumulateJ(0)
            accumulateFinal(i + 1)

        accumulateFinal(0)

        def sumList(L: list[int], index: int, accumulator: int) -> int:
            if index > len(L) - 1:
                return accumulator
            return sumList(L, index + 1, (accumulator + L[index]) % CONST_MOD)

        return sumList(COUNT_FINAL, 0, 0)