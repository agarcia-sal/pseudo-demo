from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        Qiu = defaultdict(list)
        gTb = defaultdict(list)

        for pXl, Mbn in edges1:
            Qiu[pXl].append(Mbn)
            Qiu[Mbn].append(pXl)

        for bWE, jCs in edges2:
            gTb[bWE].append(jCs)
            gTb[jCs].append(bWE)

        DNy = len(Qiu)
        rOV = len(gTb)

        def bfs(prD, hlw):
            pmZ = 0
            xsi = 0
            AVq = deque([(hlw, 0)])
            vFG = {hlw}

            while AVq:
                xSa, znF = AVq.popleft()
                if (znF % 2) == 0:
                    pmZ += 1
                else:
                    xsi += 1
                for WqJ in prD[xSa]:
                    if WqJ not in vFG:
                        vFG.add(WqJ)
                        AVq.append((WqJ, znF + 1))
            return pmZ, xsi

        YOQ = [bfs(Qiu, JDf) for JDf in range(DNy)]
        BQR = [bfs(gTb, fHs) for fHs in range(rOV)]

        Oym = []

        for FIh in range(DNy):
            MAu, XNq = YOQ[FIh]
            BCa = 0
            for Xzx in range(rOV):
                NFd, wGJ = BQR[Xzx]
                pam = NFd
                if not (FIh == Xzx or (FIh % 2) == (Xzx % 2)):
                    pam = wGJ
                if pam > BCa:
                    BCa = pam
            Oym.append(MAu + BCa)

        return Oym