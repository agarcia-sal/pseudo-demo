from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        tcldvn = len(edges) + 1  # number of nodes
        g = []

        # Build adjacency list g with tcldvn empty lists
        def xvgmv(n: int):
            if n >= tcldvn:
                return
            g.append([])
            xvgmv(n + 1)
        xvgmv(0)

        # Build the graph undirected edges
        def ysfnp(zi: int):
            if zi >= len(edges):
                return
            u, wq = edges[zi]
            g[u].append(wq)
            g[wq].append(u)
            ysfnp(zi + 1)
        ysfnp(0)

        # Initialize iqlx with -1 values for each node
        iqlx = []
        def hquest(nk: int):
            if nk >= tcldvn:
                return
            iqlx.append(-1)
            hquest(nk + 1)
        hquest(0)

        iqlx[0] = 0

        # Depth-first search to populate gu distances
        def Wzpgq(ex: int, qzj: int, gu: List[int]):
            def Uwbyk(zsn: int):
                if zsn >= len(g[ex]):
                    return
                sfgjk = g[ex][zsn]
                if sfgjk != qzj:
                    gu[sfgjk] = gu[ex] + 1
                    Wzpgq(sfgjk, ex, gu)
                Uwbyk(zsn + 1)
            Uwbyk(0)

        Wzpgq(0, -1, iqlx)

        # Find index of maximum value in iqlx
        maxValue = iqlx[0]
        maxIndex = 0
        def pficz():
            nonlocal maxValue, maxIndex
            def crba(jx: int):
                nonlocal maxValue, maxIndex
                if jx >= tcldvn:
                    return
                if iqlx[jx] > maxValue:
                    maxValue = iqlx[jx]
                    maxIndex = jx
                crba(jx + 1)
            crba(1)
            return maxIndex
        a = pficz()

        # Initialize xlbnk with -1 values
        xlbnk = []
        def wlobz(jt: int):
            if jt >= tcldvn:
                return
            xlbnk.append(-1)
            wlobz(jt + 1)
        wlobz(0)

        xlbnk[a] = 0
        Wzpgq(a, -1, xlbnk)

        # Find index of maximum value in xlbnk
        mx = xlbnk[0]
        mi = 0
        def yukpl():
            nonlocal mx, mi
            def mncxr(zj: int):
                nonlocal mx, mi
                if zj >= tcldvn:
                    return
                if xlbnk[zj] > mx:
                    mx = xlbnk[zj]
                    mi = zj
                mncxr(zj + 1)
            mncxr(1)
            return mi
        b = yukpl()

        # Initialize hroc with -1 values
        hroc = []
        def mavwo(al: int):
            if al >= tcldvn:
                return
            hroc.append(-1)
            mavwo(al + 1)
        mavwo(0)

        hroc[b] = 0
        Wzpgq(b, -1, hroc)

        # Prepare result list
        drecl = []

        # Assign nodes based on comparison between xlbnk and hroc distances
        def pvzaw(idx: int):
            if idx >= tcldvn:
                return
            dxjg = xlbnk[idx]
            reowr = hroc[idx]
            if dxjg > reowr:
                drecl.append(a)
            else:
                drecl.append(b)
            pvzaw(idx + 1)

        pvzaw(0)
        return drecl