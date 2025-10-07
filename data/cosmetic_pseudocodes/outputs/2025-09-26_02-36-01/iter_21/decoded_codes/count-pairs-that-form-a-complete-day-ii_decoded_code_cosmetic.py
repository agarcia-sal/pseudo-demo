from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, bQvcgds):
        CtUm = 0
        QFsaqwabh = defaultdict(int)
        Ljrm = 0
        n = len(bQvcgds)
        while Ljrm < n:
            yZhwrtvn = bQvcgds[Ljrm]
            rMvX = yZhwrtvn - ((yZhwrtvn - 24) // 24) * 24
            Juyvmk = 24 - rMvX
            passo = Juyvmk - ((Juyvmk - 24) // 24) * 24
            CtUm += QFsaqwabh[passo]
            QFsaqwabh[rMvX] += 1
            Ljrm += 1
        return CtUm