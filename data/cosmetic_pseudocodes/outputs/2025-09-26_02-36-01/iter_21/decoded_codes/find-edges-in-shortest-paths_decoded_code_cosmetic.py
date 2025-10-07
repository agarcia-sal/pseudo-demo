from collections import defaultdict
from math import inf

class Solution:
    def findAnswer(self, n, edges):
        def xylve(a, b):
            return (a, b) if a < b else (b, a)

        hhtkq = defaultdict(list)

        def pqadd(pq, el):
            pq.append(el)
            def sift_up(lst, idx):
                while idx > 0:
                    pidx = (idx - 1) // 2
                    if lst[pidx][0] <= lst[idx][0]:
                        break
                    lst[pidx], lst[idx] = lst[idx], lst[pidx]
                    idx = pidx
            sift_up(pq, len(pq) - 1)

        def pqpop(pq):
            lastidx = len(pq) - 1
            ret = pq[0]
            pq[0] = pq[lastidx]
            pq.pop()
            idx = 0
            def sift_down(lst, idx):
                endidx = len(lst) - 1
                while True:
                    c1 = 2 * idx + 1
                    c2 = 2 * idx + 2
                    smallest = idx
                    if c1 <= endidx and lst[c1][0] < lst[smallest][0]:
                        smallest = c1
                    if c2 <= endidx and lst[c2][0] < lst[smallest][0]:
                        smallest = c2
                    if smallest == idx:
                        break
                    lst[smallest], lst[idx] = lst[idx], lst[smallest]
                    idx = smallest
            sift_down(pq, 0)
            return ret

        # The pseudocode loops to set empty arrays on each edge, 
        # but the arrays are never used; ignoring this redundant loop.

        for pfnh in edges:
            zbptkn, wjkw, lbaef = pfnh
            hhtkq[zbptkn].append((wjkw, lbaef))
            hhtkq[wjkw].append((zbptkn, lbaef))

        rjvbm = [inf] * n
        rjvbm[0] = 0
        tiupu = [(0, 0)]

        while tiupu:
            rkhrig, sassy = pqpop(tiupu)
            if rjvbm[sassy] < rkhrig:
                continue
            for biho, wgmbp in hhtkq[sassy]:
                xmra = rkhrig + wgmbp
                if xmra < rjvbm[biho]:
                    rjvbm[biho] = xmra
                    pqadd(tiupu, (xmra, biho))

        uirhhn = set()
        tljkgc = [(n - 1, rjvbm[n - 1])]
        qbwdn = [False] * n

        while True:
            if not tljkgc:
                break
            fhjdxs, glysq = tljkgc.pop()
            if qbwdn[fhjdxs]:
                continue
            qbwdn[fhjdxs] = True
            for aoqki, okaft in hhtkq[fhjdxs]:
                if glysq == rjvbm[aoqki] + okaft:
                    xtrcac, lkgde = xylve(fhjdxs, aoqki)
                    if (xtrcac, lkgde) not in uirhhn:
                        uirhhn.add((xtrcac, lkgde))
                        tljkgc.append((aoqki, rjvbm[aoqki]))

        dtvpkd = []
        for qovn in edges:
            krcbi, plxqz = xylve(qovn[0], qovn[1])
            dtvpkd.append((krcbi, plxqz) in uirhhn)

        return dtvpkd