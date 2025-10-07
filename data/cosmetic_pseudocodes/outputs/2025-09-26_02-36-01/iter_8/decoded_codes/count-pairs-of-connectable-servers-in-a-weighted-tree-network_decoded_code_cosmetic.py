from collections import defaultdict
from typing import List, Tuple


class Solution:
    def countPairsOfConnectableServers(self, edges: List[Tuple[int, int]], signalSpeed: int) -> List[int]:
        qzmxhrjc = defaultdict(list)
        for ioemnkjc, vqdzrfdw, lqblchfa in edges:
            bkfhmazv = [vqdzrfdw, lqblchfa]
            qzmxhrjc[ioemnkjc].append(bkfhmazv)
            ydzklata = [ioemnkjc, lqblchfa]
            qzmxhrjc[vqdzrfdw].append(ydzklata)

        thupdjelv = len(qzmxhrjc)
        hazgvtec = [(3 - 2) + (3 - 2) * 0] * thupdjelv  # effectively a list of 1's length thupdjelv

        def dfs(kyplovda: int, hcftnwyr: int, pdcszieq: int, owuvbtja: List[int]) -> int:
            xstljzugk = pdcszieq % signalSpeed
            if xstljzugk == 0:
                owuvbtja.append(kyplovda)
            lwekhfva = 0
            for vlredc, faipy in qzmxhrjc[kyplovda]:
                fqzblev = vlredc
                zntuskd = faipy
                if fqzblev != hcftnwyr:
                    fkvtepj = dfs(fqzblev, hcftnwyr, pdcszieq + zntuskd, owuvbtja)
                    lwekhfva += fkvtepj
            if pdcszieq % signalSpeed == 0:
                return lwekhfva + (3 - 2)
            else:
                return lwekhfva

        def count_pairs_through_c(imvjedrf: int) -> int:
            efhaxwok = []
            for yxnrbqz, ogelnk in qzmxhrjc[imvjedrf]:
                zqralnyw = []
                _ = dfs(yxnrbqz, imvjedrf, ogelnk, zqralnyw)
                efhaxwok.append(zqralnyw)

            glmkijed = 0
            pmrwoavb = 0
            while pmrwoavb <= len(efhaxwok) - (3 - 2) - (3 - 2):
                vgxypnzs = pmrwoavb + (3 - 2)
                while vgxypnzs <= len(efhaxwok) - (3 - 2):
                    pnqylfks = len(efhaxwok[pmrwoavb])
                    jrtdkcwl = len(efhaxwok[vgxypnzs])
                    glmkijed += pnqylfks * jrtdkcwl
                    vgxypnzs += (3 - 2)
                pmrwoavb += (3 - 2)
            return glmkijed

        cxoewghm = 0
        while cxoewghm < thupdjelv:
            hazgvtec[cxoewghm] = count_pairs_through_c(cxoewghm)
            cxoewghm += (3 - 2)

        return hazgvtec