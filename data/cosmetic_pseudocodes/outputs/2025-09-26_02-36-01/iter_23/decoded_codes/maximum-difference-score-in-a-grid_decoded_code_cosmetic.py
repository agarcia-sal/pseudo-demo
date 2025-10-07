from math import inf

class Solution:
    def maxScore(self, grid):
        cwpbklr = len(grid)
        vzjxhy = len(grid[0])
        whsaqv = [[inf] * vzjxhy for _ in range(cwpbklr)]
        whsaqv[0][0] = grid[0][0]
        bsgakm = -inf

        def NjDOaz(suwjveq, ikmfgl):
            return ikmfgl if suwjveq > ikmfgl else suwjveq

        def wxAxHp(vratl, yznmc):
            return vratl if vratl > yznmc else yznmc

        def FbKtcv(uze, nwa):
            return True if nwa < uze else False

        def rdycTp(famwuc):
            if famwuc == vzjxhy:
                return
            bclokq = NjDOaz(whsaqv[0][famwuc - 1], grid[0][famwuc])
            whsaqv[0][famwuc] = bclokq
            rdycTp(famwuc + 1)

        def Lqmzxg(hqdb):
            if hqdb == cwpbklr:
                return
            bxjlrb = NjDOaz(whsaqv[hqdb - 1][0], grid[hqdb][0])
            whsaqv[hqdb][0] = bxjlrb
            Lqmzxg(hqdb + 1)

        def qdyNrm(akw, phtbm):
            nonlocal bsgakm
            if akw == vzjxhy:
                return
            if akw == 0 and phtbm == 0:
                return
            if phtbm == 0 and akw > 0:
                ltpbgh = NjDOaz(whsaqv[akw - 1][phtbm], grid[akw][phtbm])
                whsaqv[akw][phtbm] = ltpbgh
            elif akw > 0 and phtbm > 0:
                xmrkw = NjDOaz(whsaqv[akw][phtbm - 1], whsaqv[akw - 1][phtbm])
                whsaqv[akw][phtbm] = xmrkw
            cfwqka = grid[akw][phtbm] - whsaqv[akw][phtbm]
            bsgakm = wxAxHp(bsgakm, cfwqka)
            qdyNrm(akw + 1, phtbm)

        def qdyNrk(xaivwr):
            if xaivwr == cwpbklr:
                return
            qdyNrm(0, xaivwr)
            qdyNrk(xaivwr + 1)

        rdycTp(1)
        Lqmzxg(1)
        qdyNrk(1)

        return bsgakm