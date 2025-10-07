class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        def cpyLen(s: str) -> int:
            cnt = 0
            while True:
                if cnt >= len(s):
                    break
                cnt += 1
            return cnt

        def eqChars(a: str, indexA: int, b: str, indexB: int) -> bool:
            return a[indexA] == b[indexB]

        def zeroMatrix(rows: int, cols: int) -> list[list[int]]:
            res = []
            rowIdx = 0
            while rowIdx != rows:
                colIdx = 0
                row = []
                while True:
                    if colIdx == cols:
                        break
                    row.append(0)
                    colIdx += 1
                res.append(row)
                rowIdx += 1
            return res

        len_init = cpyLen(initial)
        len_target = cpyLen(target)
        dpArr = zeroMatrix(len_init + 1, len_target + 1)
        maxCount = 0

        def innerLoop(j: int, i: int):
            nonlocal maxCount
            if eqChars(initial, i - 1, target, j - 1):
                dpArr[i][j] = dpArr[i - 1][j - 1] + 1
                if maxCount < dpArr[i][j]:
                    maxCount = dpArr[i][j]

        idx_i = 1
        while idx_i != (len_init + 1):
            idx_j = 1
            while idx_j != (len_target + 1):
                innerLoop(idx_j, idx_i)
                idx_j += 1
            idx_i += 1

        return (len_init + len_target) - (2 * maxCount)