from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        a = 0
        b = len(grid)
        c = len(grid[0]) if b > 0 else 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i_outer = 0

        while i_outer < b:
            j_inner = 0
            while j_inner < c:
                if grid[i_outer][j_inner] == 1:
                    k1 = 0
                    m1 = 0
                    while k1 < c:
                        if k1 != j_inner:
                            m1 += grid[i_outer][k1]
                        k1 += 1

                    k2 = 0
                    m2 = 0
                    while k2 < b:
                        if k2 != i_outer:
                            m2 += grid[k2][j_inner]
                        k2 += 1

                    d += m1 * m2
                j_inner += 1
            i_outer += 1
        return d