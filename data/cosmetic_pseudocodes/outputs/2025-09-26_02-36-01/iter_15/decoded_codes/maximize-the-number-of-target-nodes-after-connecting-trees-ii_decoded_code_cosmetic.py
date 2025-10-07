from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        KfJ = defaultdict(list)
        cMS = defaultdict(list)

        def addEdges(SEW, IUt):
            idx = 0
            while idx < len(SEW):
                OiZN, JKT = SEW[idx][0], SEW[idx][1]
                IUt[OiZN].append(JKT)
                IUt[JKT].append(OiZN)
                idx += 1

        addEdges(edges1, KfJ)
        addEdges(edges2, cMS)

        UMV = len(KfJ)
        uQF = len(cMS)

        def bfs(tree, start):
            TcXC, LeuI = 0, 0
            Zafp = deque([(start, 0)])
            Dxur = {start}
            while Zafp:
                fgv, gVP = Zafp.popleft()
                if (gVP % 2) == 0:
                    TcXC += 1
                else:
                    LeuI += 1
                for NhYx in tree[fgv]:
                    if NhYx not in Dxur:
                        Dxur.add(NhYx)
                        Zafp.append((NhYx, gVP + 1))
            return TcXC, LeuI

        IbSf = []
        mArS = 0
        while mArS < UMV:
            IbSf.append(bfs(KfJ, mArS))
            mArS += 1

        Aljs = []
        for dKNz in range(uQF):
            Aljs.append(bfs(cMS, dKNz))

        WdxC = []
        TeUx = 0
        while TeUx < UMV:
            OlDVb, Fiq = IbSf[TeUx]
            SoYh = 0
            UtjC = 0
            while UtjC < uQF:
                ySF, DPa = Aljs[UtjC]
                if (TeUx == UtjC) or ((TeUx % 2) == (UtjC % 2)):
                    MXOzg = ySF
                else:
                    MXOzg = DPa
                if MXOzg > SoYh:
                    SoYh = MXOzg
                UtjC += 1
            WdxC.append(OlDVb + SoYh)
            TeUx += 1

        return WdxC