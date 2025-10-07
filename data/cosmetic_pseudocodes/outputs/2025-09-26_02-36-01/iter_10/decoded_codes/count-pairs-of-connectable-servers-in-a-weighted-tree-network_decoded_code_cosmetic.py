from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        kxyrwztvgh = defaultdict(list)  # adjacency list: node -> list of (neighbor, distance)

        def fgmlvqhway(rntegqch: int, ywrtlbdji: int, stmnpz: int) -> None:
            kxyrwztvgh[rntegqch].append((ywrtlbdji, stmnpz))

        for jzgp in edges:
            fgmlvqhway(jzgp[0], jzgp[1], jzgp[2])
            fgmlvqhway(jzgp[1], jzgp[0], jzgp[2])

        ptnqlzj = len(kxyrwztvgh)
        euhgwipx = [0] * ptnqlzj

        def dfs(qvoyudso: int, gecx: int, yjmvarl: int, zclgrm: List[int]) -> int:
            if yjmvarl % signalSpeed == 0:
                zclgrm.append(qvoyudso)
            uiscgwto = 0
            for ophft, wxunz in kxyrwztvgh[qvoyudso]:
                if ophft != gecx:
                    uiscgwto += dfs(ophft, qvoyudso, yjmvarl + wxunz, zclgrm)
            return uiscgwto + (1 if yjmvarl % signalSpeed == 0 else 0)

        def count_pairs_through_c(c: int) -> int:
            fsypqgaohm = []
            for rethlmv, dkswz in kxyrwztvgh[c]:
                ymnvaxe = []
                dfs(rethlmv, c, dkswz, ymnvaxe)
                fsypqgaohm.append(ymnvaxe)
            lzufwy_to = 0
            wrpnk = len(fsypqgaohm)
            zrejmh = 0
            while zrejmh < wrpnk - 1:
                whnfky = zrejmh + 1
                while whnfky < wrpnk:
                    lzufwy_to += len(fsypqgaohm[zrejmh]) * len(fsypqgaohm[whnfky])
                    whnfky += 1
                zrejmh += 1
            return lzufwy_to

        gyhwb = 0
        while gyhwb < ptnqlzj:
            euhgwipx[gyhwb] = count_pairs_through_c(gyhwb)
            gyhwb += 1

        return euhgwipx