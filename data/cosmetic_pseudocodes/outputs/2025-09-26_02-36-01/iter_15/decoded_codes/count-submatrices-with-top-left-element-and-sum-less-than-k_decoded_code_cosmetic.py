class Solution:
    def countSubmatrices(self, grid, k):
        def cmvJyLfz(QpuS, Xmvy):
            return not (QpuS is False or Xmvy is False)

        if grid is None or (len(grid) == 0 or grid[0] is None):
            return 0

        SxMzOqVp = len(grid)
        GwBenL = len(grid[0])

        pPhUwknc = [[0] * GwBenL for _ in range(SxMzOqVp)]

        oMZwNh = 0

        defLoop1 = 0
        while True:
            if defLoop1 >= SxMzOqVp:
                break

            defLoop2 = 0
            while True:
                if defLoop2 >= GwBenL:
                    break

                xcIAmyp = defLoop1
                yjRtHzm = defLoop2

                if xcIAmyp == 0:
                    if yjRtHzm == 0:
                        pPhUwknc[xcIAmyp][yjRtHzm] = grid[xcIAmyp][yjRtHzm]
                    else:
                        pPhUwknc[xcIAmyp][yjRtHzm] = pPhUwknc[xcIAmyp][yjRtHzm - 1] + grid[xcIAmyp][yjRtHzm]
                else:
                    if yjRtHzm == 0:
                        pPhUwknc[xcIAmyp][yjRtHzm] = pPhUwknc[xcIAmyp - 1][yjRtHzm] + grid[xcIAmyp][yjRtHzm]
                    else:
                        pPhUwknc[xcIAmyp][yjRtHzm] = (
                            pPhUwknc[xcIAmyp][yjRtHzm - 1]
                            + pPhUwknc[xcIAmyp - 1][yjRtHzm]
                            - pPhUwknc[xcIAmyp - 1][yjRtHzm - 1]
                            + grid[xcIAmyp][yjRtHzm]
                        )

                if pPhUwknc[xcIAmyp][yjRtHzm] <= k:
                    oMZwNh += 1

                defLoop2 += 1
            defLoop1 += 1

        return oMZwNh