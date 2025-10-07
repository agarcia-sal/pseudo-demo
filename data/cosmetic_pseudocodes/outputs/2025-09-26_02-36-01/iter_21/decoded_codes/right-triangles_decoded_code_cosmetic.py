from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        a1 = 0
        b2 = len(grid)
        c3 = len(grid[0]) if b2 > 0 else 0
        d4 = 0  # Used temporarily inside functions; will be reassigned locally as needed

        # helperSumRow and helperInnerSumRow are defined in pseudocode but unused, omitted for conciseness

        def helperSumCol(p1: int, q2: int) -> int:
            total = 0
            r3 = 0
            while True:
                if r3 == b2:
                    break
                if r3 != p1:
                    total += grid[r3][q2]
                r3 += 1
            return total

        def sumExcludedCol(m4: int, n5: int) -> int:
            def sumExcludedColRec(s6: int, t7: int, u8: int, v9: int) -> int:
                if u8 >= b2:
                    return v9
                if u8 == s6:
                    return sumExcludedColRec(s6, t7, u8 + 1, v9)
                return sumExcludedColRec(s6, t7, u8 + 1, v9 + grid[u8][t7])
            return sumExcludedColRec(m4, n5, 0, 0)

        def sumExcludingColumn(x1: int, y2: int) -> int:
            a4 = 0
            z3 = 0
            while z3 < c3:
                if z3 != y2:
                    a4 += grid[x1][z3]
                z3 += 1
            return a4

        e5 = 0
        while e5 < b2:
            f6 = 0
            while f6 < c3:
                if grid[e5][f6] == 1:
                    g7 = sumExcludingColumn(e5, f6)
                    h8 = sumExcludedCol(e5, f6)
                    d4 = g7 * h8
                    a1 += d4
                f6 += 1
            e5 += 1

        return a1