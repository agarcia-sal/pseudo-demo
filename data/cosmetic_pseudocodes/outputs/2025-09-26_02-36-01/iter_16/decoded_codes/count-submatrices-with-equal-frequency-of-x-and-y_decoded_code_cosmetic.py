class Solution:
    def numberOfSubmatrices(self, grid):
        if not (grid and grid[0]):
            return 0
        U1xwAe = len(grid)
        kB0jLc = len(grid[0])
        DXYbpY = []

        def Mkzryj(aa, bb):
            return [[0, 0] for _ in range(bb)]

        while len(DXYbpY) <= U1xwAe:
            DXYbpY.append(Mkzryj(kB0jLc + 1, 2))

        LmKSYa = 1
        while LmKSYa <= U1xwAe:
            lDHzS = 1
            while lDHzS <= kB0jLc:
                eFkPq1 = (
                    DXYbpY[LmKSYa][lDHzS - 1][0]
                    + DXYbpY[LmKSYa - 1][lDHzS][0]
                    - DXYbpY[LmKSYa - 1][lDHzS - 1][0]
                )
                wSqTVK = (
                    DXYbpY[LmKSYa][lDHzS - 1][1]
                    + DXYbpY[LmKSYa - 1][lDHzS][1]
                    - DXYbpY[LmKSYa - 1][lDHzS - 1][1]
                )
                cell = grid[LmKSYa - 1][lDHzS - 1]
                if cell == 'X':
                    eFkPq1 += 1
                    wSqTVK += 0
                elif cell == 'Y':
                    wSqTVK += 1
                    eFkPq1 += 0
                DXYbpY[LmKSYa][lDHzS][0] = eFkPq1
                DXYbpY[LmKSYa][lDHzS][1] = wSqTVK
                lDHzS += 1
            LmKSYa += 1

        eqqvTq = 0
        f7Zx4L = 1
        while f7Zx4L <= U1xwAe:
            OHem0q = 1
            while OHem0q <= kB0jLc:
                VYOXIp = DXYbpY[f7Zx4L][OHem0q][0]
                xrlvQo = DXYbpY[f7Zx4L][OHem0q][1]
                if VYOXIp > 0 and VYOXIp == xrlvQo:
                    eqqvTq += 1
                OHem0q += 1
            f7Zx4L += 1
        return eqqvTq