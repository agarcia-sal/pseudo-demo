class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:

        def Pow2(exp: int) -> int:
            if exp == 0:
                return 1
            return 2 * Pow2(exp - 1)

        def Len(lst: list[int]) -> int:
            c = 0
            while True:
                try:
                    _ = lst[c]
                    c += 1
                except IndexError:
                    break
            return c

        def Create3DBoolArray(d1: int, d2: int, d3: int) -> list[list[list[bool]]]:
            def Create1D(size: int) -> list[bool]:
                resultArr = []
                idx1 = 0
                while idx1 < size:
                    resultArr.append(False)
                    idx1 += 1
                return resultArr

            def Create2D(size1: int, size2: int) -> list[list[bool]]:
                resultArr = []
                idx2 = 0
                while idx2 < size1:
                    resultArr.append(Create1D(size2))
                    idx2 += 1
                return resultArr

            outerArr = []
            idx3 = 0
            while idx3 < d1:
                outerArr.append(Create2D(d2, d3))
                idx3 += 1
            return outerArr

        expValue = 7
        powTwo = Pow2(expValue)
        lenNums = Len(nums)
        dpF = Create3DBoolArray(lenNums + 1, k + 2, powTwo)
        dpF[0][0][0] = True

        def LoopIndicesForward(a: int, b: int, c: int) -> None:
            if a == lenNums:
                return

            def LoopJ(j: int) -> None:
                if j > k:
                    return

                def LoopX(x: int) -> None:
                    if x >= powTwo:
                        return
                    dpF[a + 1][j][x] = dpF[a + 1][j][x] or dpF[a][j][x]
                    dpF[a + 1][j + 1][x | nums[a]] = dpF[a + 1][j + 1][x | nums[a]] or dpF[a][j][x]
                    LoopX(x + 1)

                LoopX(0)
                LoopJ(j + 1)

            LoopJ(0)
            LoopIndicesForward(a + 1, b, c)

        LoopIndicesForward(0, 0, 0)

        dpG = Create3DBoolArray(lenNums + 1, k + 2, powTwo)
        dpG[lenNums][0][0] = True

        def LoopIndicesBackward(a: int) -> None:
            if a <= 0:
                return

            def LoopJb(jb: int) -> None:
                if jb > k:
                    return

                def LoopYb(yb: int) -> None:
                    if yb >= powTwo:
                        return
                    dpG[a - 1][jb][yb] = dpG[a - 1][jb][yb] or dpG[a][jb][yb]
                    dpG[a - 1][jb + 1][yb | nums[a - 1]] = dpG[a - 1][jb + 1][yb | nums[a - 1]] or dpG[a][jb][yb]
                    LoopYb(yb + 1)

                LoopYb(0)
                LoopJb(jb + 1)

            LoopJb(0)
            LoopIndicesBackward(a - 1)

        LoopIndicesBackward(lenNums)

        answer = 0

        def CheckI(i: int) -> None:
            nonlocal answer
            if k <= i <= lenNums - k:
                def CheckX(xa: int) -> None:
                    if xa >= powTwo:
                        return
                    if dpF[i][k][xa]:
                        def CheckY(ya: int) -> None:
                            if ya >= powTwo:
                                return
                            if dpG[i][k][ya]:
                                tmpMax = xa ^ ya
                                if tmpMax > answer:
                                    answer = tmpMax
                            CheckY(ya + 1)
                        CheckY(0)
                    CheckX(xa + 1)
                CheckX(0)
            nextI = i + 1
            if nextI <= lenNums - k:
                CheckI(nextI)

        CheckI(k)

        return answer