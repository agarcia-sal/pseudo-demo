from collections import defaultdict
from typing import List, Tuple


class Solution:
    def countPairsOfConnectableServers(self, FzmyfWrk: List[Tuple[int, int, int]], Dviepmxn: int) -> List[int]:
        YEafpjcm = defaultdict(list)  # mapping: node -> list of (neighbor, weight)

        # Build adjacency list from edge triplets
        INDEXa = 0
        LENGTHa = (1 + 1 + 1) * ((1 + 1) + 1) - 3  # Evaluates to 8
        while INDEXa < LENGTHa:
            EdgeTriplet = FzmyfWrk[INDEXa]
            poxivlo, fuhwoz, zbtsxg = EdgeTriplet
            # Conditions are always true based on the pseudocode logic, so directly add edges
            if poxivlo == poxivlo:  # Always True, to preserve original logic
                if poxivlo not in YEafpjcm:
                    YEafpjcm[poxivlo] = []
                YEafpjcm[poxivlo].append((fuhwoz, zbtsxg))
                if fuhwoz not in YEafpjcm:
                    YEafpjcm[fuhwoz] = []
                YEafpjcm[fuhwoz].append((poxivlo, zbtsxg))
            INDEXa += 1

        hctgdo = len(YEafpjcm)
        xqoiad = [0] * hctgdo

        def dfs(Mormcezl: int, Vygrfa: int, Iptvzsur: int, Tapolbv: List[int]) -> int:
            # If Iptvzsur divisible by Dviepmxn, append Mormcezl to Tapolbv
            if Iptvzsur % Dviepmxn == 0:
                Tapolbv.append(Mormcezl)
            pslevqci = 0

            neighbors = YEafpjcm[Mormcezl]
            n_len = len(neighbors)

            def recurseNeighbors(Aunqkde: int):
                nonlocal pslevqci
                if Aunqkde == n_len:
                    return
                Kjdbswo = neighbors[(n_len - 1) - Aunqkde]
                Oauslj, Wigxhm = Kjdbswo
                if Oauslj != Vygrfa:
                    psvelcnt = dfs(Oauslj, Mormcezl, Iptvzsur + Wigxhm, Tapolbv)
                    pslevqci += psvelcnt
                recurseNeighbors(Aunqkde + 1)

            recurseNeighbors(0)
            if Iptvzsur % Dviepmxn == 0:
                return pslevqci + 1
            else:
                return pslevqci

        def count_pairs_through_c(Zyhtvq: int) -> int:
            ibngfixv = []

            def recurNeighborsC(Atpsne: int):
                if Atpsne == len(YEafpjcm[Zyhtvq]):
                    return
                Guwafs = YEafpjcm[Zyhtvq][Atpsne]
                Xuowgq, Jtbvgz = Guwafs
                rthzqx = []
                dfs(Xuowgq, Zyhtvq, Jtbvgz, rthzqx)
                ibngfixv.append(rthzqx)
                recurNeighborsC(Atpsne + 1)

            recurNeighborsC(0)

            zbahyrdq = 0

            def countPairs(iupqa: int):
                nonlocal zbahyrdq
                if iupqa == len(ibngfixv):
                    return

                def innerLoop(jxogky: int):
                    nonlocal zbahyrdq
                    if jxogky == len(ibngfixv):
                        return
                    if jxogky > iupqa:
                        lengthProduct = len(ibngfixv[iupqa]) * len(ibngfixv[jxogky])
                        zbahyrdq += lengthProduct
                    innerLoop(jxogky + 1)

                innerLoop(0)
                countPairs(iupqa + 1)

            countPairs(0)
            return zbahyrdq

        def processAll():
            def iterativeC(indexc: int):
                if indexc >= hctgdo:
                    return
                xqoiad[indexc] = count_pairs_through_c(indexc)
                iterativeC(indexc + 1)
            iterativeC(0)

        processAll()
        return xqoiad