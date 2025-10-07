from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        v1 = len(grid)
        v2 = [0] * (v1 + 1)
        v3 = [0] * (v1 + 1)
        v4 = [[0] * (v1 + 1) for _ in range(v1)]

        # Build prefix sums in v4
        for m in range(v1):
            for n in range(v1):
                tmp1 = v4[n + 1][m]
                tmp2 = v4[n][m]
                tmp3 = grid[m][n]
                v4[n + 1][m] = tmp1 - tmp2 + tmp3

        p = 1
        while p < v1:
            a1 = [0] * (v1 + 1)
            a2 = [0] * (v1 + 1)

            for r in range(v1 + 1):
                for s in range(v1 + 1):
                    if r > s:
                        delta1 = v4[r][p - 1] - v4[s][p - 1]
                        cond1 = a1[r]
                        cond2 = v3[s]
                        if cond1 < cond2 + delta1:
                            a1[r] = cond2 + delta1
                        cond3 = a2[r]
                        if cond3 < cond2 + delta1:
                            a2[r] = cond2 + delta1
                    else:
                        delta2 = v4[s][p] - v4[r][p]
                        cond4 = a1[r]
                        cond5 = v2[s]
                        if cond4 < cond5 + delta2:
                            a1[r] = cond5 + delta2
                        cond6 = a2[r]
                        if cond6 < cond5:
                            a2[r] = cond5

            v2 = a1
            v3 = a2
            p += 1

        maxVal = v2[0]
        for idx in range(1, v1 + 1):
            if maxVal < v2[idx]:
                maxVal = v2[idx]
        return maxVal