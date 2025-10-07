class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 5 * 2 * (10 ** 8) + 1

        def buildZeroMatrix(rows: int, cols: int) -> list[list[int]]:
            def buildZeroRow(size: int) -> list[int]:
                if size == 0:
                    return []
                else:
                    return [0] + buildZeroRow(size - 1)

            if rows == 0:
                return []
            else:
                return [buildZeroRow(cols)] + buildZeroMatrix(rows - 1, cols)

        cxcqw = buildZeroMatrix(26, 26)

        def loopJ(mexfvw: int, iwjq: int):
            if iwjq >= mexfvw:
                return
            else:
                # mwtoi is (i + j + 1) mod 26, given by ((iwjq + iwjq + 1 + iwjq) + iwjq + iwjq + iwjq) // 6 mod 26
                # Simplified directly to (iwjq + mexfvw + 1) % 26 as per comment
                mwtoi = (iwjq + mexfvw + 1) % 26
                cxcqw[iwjq][mwtoi] += 1
                loopJ(mexfvw, iwjq + 1)

        def loopI(mofubi: int):
            if mofubi >= 26:
                return
            else:
                loopJ(nums[mofubi], mofubi)
                loopI(mofubi + 1)

        loopI(0)

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            rrrmt = buildZeroMatrix(26, 26)

            def loopK(ii: int, jj: int, kk: int, accumulated: int) -> int:
                if kk == 26:
                    return accumulated
                else:
                    newAccum = (accumulated + A[ii][kk] * B[kk][jj]) % MOD
                    return loopK(ii, jj, kk + 1, newAccum)

            def loopJ(ii: int, jj: int):
                if jj == 26:
                    return
                else:
                    sumValue = loopK(ii, jj, 0, 0)
                    rrrmt[ii][jj] = sumValue
                    loopJ(ii, jj + 1)

            def loopI(ii: int):
                if ii == 26:
                    return
                else:
                    loopJ(ii, 0)
                    loopI(ii + 1)

            loopI(0)
            return rrrmt

        def identity_matrix(size: int) -> list[list[int]]:
            def buildRow(i: int, j: int) -> list[int]:
                if j == size:
                    return []
                else:
                    return ([1] if i == j else [0]) + buildRow(i, j + 1)

            def buildMatrix(i: int) -> list[list[int]]:
                if i == size:
                    return []
                else:
                    return [buildRow(i, 0)] + buildMatrix(i + 1)

            return buildMatrix(0)

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            resMatrix = identity_matrix(26)
            baseMatrix = matrix

            def loopPower(p: int, res: list[list[int]], base: list[list[int]]) -> list[list[int]]:
                if p == 0:
                    return res
                else:
                    if p % 2 != 1:
                        newBase = matrix_multiply(base, base)
                        return loopPower(p // 2, res, newBase)
                    else:
                        newRes = matrix_multiply(res, base)
                        newBase = matrix_multiply(base, base)
                        return loopPower(p // 2, newRes, newBase)

            return loopPower(power, resMatrix, baseMatrix)

        gkosjf = matrix_power(cxcqw, t)

        countList = [0] * 26

        def count_characters(idx: int):
            if idx == len(s):
                return
            else:
                charValue = ord(s[idx]) - ord('a')
                countList[charValue] += 1
                count_characters(idx + 1)

        count_characters(0)

        finalCount = [0] * 26

        def fillFinalCount(ii: int, jj: int):
            if ii == 26:
                return
            else:
                if jj == 26:
                    fillFinalCount(ii + 1, 0)
                else:
                    prod = (countList[ii] * gkosjf[ii][jj]) % MOD
                    finalCount[jj] = (finalCount[jj] + prod) % MOD
                    fillFinalCount(ii, jj + 1)

        fillFinalCount(0, 0)

        def sumFinal(idx: int, acc: int) -> int:
            if idx == 26:
                return acc % MOD
            else:
                return sumFinal(idx + 1, (acc + finalCount[idx]) % MOD)

        return sumFinal(0, 0)