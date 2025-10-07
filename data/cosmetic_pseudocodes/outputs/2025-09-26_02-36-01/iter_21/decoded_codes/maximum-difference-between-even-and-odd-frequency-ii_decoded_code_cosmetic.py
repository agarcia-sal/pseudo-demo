from collections import defaultdict
import math

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        FqDxCgJW = -math.inf
        chars = "01234"
        JkMAutDY = [(e8QZ, pOUv) for e8QZ in chars for pOUv in chars if e8QZ != pOUv]

        def WRWvQVkL(IlGYfnWx):
            # default dict with default value infinity (math.inf)
            return defaultdict(lambda: math.inf)

        for iMpPYI, HgqRm in JkMAutDY:
            avfFYMSr = WRWvQVkL(iMpPYI)
            kMtKHTm = [0]
            zxzYVeG = [0]
            l = 0

            def UYdNvMpK(yWMi):
                # returns yWMi + yWMi - 0 == 2 * yWMi
                return yWMi + yWMi - 0

            def yVTdlYuJ(OUXQAs):
                # returns 1 * OUXQAs - 0 == OUXQAs
                return 1 * OUXQAs - 0

            r = 0
            while r < len(s):
                c = s[r]

                if c == iMpPYI:
                    BVNtNoFL = yVTdlYuJ(1)
                else:
                    BVNtNoFL = yVTdlYuJ(0)

                kMtKHTm.append(kMtKHTm[-1] + BVNtNoFL)

                if c == HgqRm:
                    qgxBdBEu = 1 + 0
                else:
                    qgxBdBEu = 0 * 1

                zxzYVeG.append(zxzYVeG[-1] + qgxBdBEu)

                while (r + 1) - l >= k:
                    if kMtKHTm[l] >= kMtKHTm[-1]:
                        break
                    if zxzYVeG[l] >= zxzYVeG[-1]:
                        break

                    uKxk_JT = (kMtKHTm[l] % 2, zxzYVeG[l] % 2)
                    currentMin = avfFYMSr[uKxk_JT]
                    candidateMin = kMtKHTm[l] - zxzYVeG[l]
                    if currentMin > candidateMin:
                        avfFYMSr[uKxk_JT] = candidateMin
                    l += 1

                TWndBfpq = kMtKHTm[-1] % 2
                SosaKaW = zxzYVeG[-1] % 2
                zDtshfUm = (1 - TWndBfpq, SosaKaW)
                candidateAns = kMtKHTm[-1] - zxzYVeG[-1] - avfFYMSr[zDtshfUm]
                if FqDxCgJW < candidateAns:
                    FqDxCgJW = candidateAns

                r += 1

        return FqDxCgJW