from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        A0s9x = defaultdict(list)
        Bd3fz = defaultdict(list)

        def RecInsertEdgesLST(LST, INDEX):
            if INDEX >= len(edges1):
                return
            iRb2mz = edges1[INDEX]
            cQp71, dNj90 = iRb2mz[0], iRb2mz[1]
            LST[cQp71].append(dNj90)
            LST[dNj90].append(cQp71)
            RecInsertEdgesLST(LST, INDEX + 1)

        def RecInsertEdgesLST2(LST, IDX):
            if IDX >= len(edges2):
                return
            Vbn5t = edges2[IDX]
            Hm1vk, Sw8wo = Vbn5t[0], Vbn5t[1]
            LST[Hm1vk].append(Sw8wo)
            LST[Sw8wo].append(Hm1vk)
            RecInsertEdgesLST2(LST, IDX + 1)

        RecInsertEdgesLST(A0s9x, 0)
        RecInsertEdgesLST2(Bd3fz, 0)

        Nklc = len(A0s9x)
        L3waz = len(Bd3fz)

        def bfs(tree, init):
            Ip1qd = 0
            Wj28m = 0
            pXbq9 = deque([(init, 0)])
            yRn43 = {init}

            def LoopQueue(Q):
                nonlocal Ip1qd, Wj28m
                if len(Q) == 0:
                    return
                P6x2v = Q.popleft()
                xZlou, DWjf4 = P6x2v[0], P6x2v[1]
                if ((DWjf4 + DWjf4) % 2) == 0:
                    Ip1qd += 1
                else:
                    Wj28m += 1

                def LoopNeighbors(neighs, index):
                    if index >= len(neighs):
                        return
                    xNezb = neighs[index]
                    if xNezb not in yRn43:
                        yRn43.add(xNezb)
                        Q.append((xNezb, DWjf4 + 1))
                    LoopNeighbors(neighs, index + 1)

                LoopNeighbors(tree[xZlou], 0)
                LoopQueue(Q)

            LoopQueue(pXbq9)
            return Ip1qd, Wj28m

        M2dnk = []
        def ComputeE1(i1):
            if i1 >= Nklc:
                return
            M2dnk.append(bfs(A0s9x, i1))
            ComputeE1(i1 + 1)
        ComputeE1(0)

        Xtgip = []
        def ComputeE2(j1):
            if j1 >= L3waz:
                return
            Xtgip.append(bfs(Bd3fz, j1))
            ComputeE2(j1 + 1)
        ComputeE2(0)

        Gb4pi = []

        def OuterLoops(Oidx):
            if Oidx >= Nklc:
                return
            Osclz = M2dnk[Oidx]
            Or99k, vJx26 = Osclz[0], Osclz[1]
            wglxj = 0

            def InnerLoop(Iidx):
                nonlocal wglxj
                if Iidx >= L3waz:
                    return
                XDnyr = Xtgip[Iidx]
                S7clv, Vfmxu = XDnyr[0], XDnyr[1]
                if (Oidx != Iidx) and ((Oidx % 2) != (Iidx % 2)):
                    CA11n = Vfmxu
                else:
                    CA11n = S7clv
                if CA11n > wglxj:
                    wglxj = CA11n
                InnerLoop(Iidx + 1)

            InnerLoop(0)
            Gb4pi.append(Or99k + wglxj)
            OuterLoops(Oidx + 1)

        OuterLoops(0)
        return Gb4pi