from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        mxybr = defaultdict(list)

        def fillGraph(idx: int) -> None:
            if idx == len(edges):
                return
            a, b, c = edges[idx][0], edges[idx][1], edges[idx][2]
            mxybr[a].append((b, c))
            mxybr[b].append((a, c))
            fillGraph(idx + 1)
        fillGraph(0)

        wwetaf = len(mxybr)
        cbvnep = [0] * wwetaf

        def explore(t: int, r: int, s: int, l: List[int]) -> int:
            ultrs = 0
            if s % signalSpeed == 0:
                l.append(t)

            def neighborIter(pairs: List[Tuple[int,int]], pos: int) -> None:
                nonlocal ultrs
                if pos == len(pairs):
                    return
                cfnwy, gquzo = pairs[pos]
                if cfnwy != r:
                    ultrs += explore(cfnwy, r, s + gquzo, l)
                neighborIter(pairs, pos + 1)

            neighborIter(mxybr[t], 0)
            return ultrs + 1 if s % signalSpeed == 0 else ultrs

        def pairsCountThrough(q: int) -> int:
            ktrux = []

            def gatherPaths(arr: List[Tuple[int,int]], idxp: int) -> None:
                if idxp == len(arr):
                    return
                vlmnt, wght = arr[idxp]
                ptth = []
                explore(vlmnt, q, wght, ptth)
                ktrux.append(ptth)
                gatherPaths(arr, idxp + 1)

            gatherPaths(mxybr[q], 0)

            totalPairs = 0

            def sumPairs(i_idx: int) -> None:
                nonlocal totalPairs
                if i_idx == len(ktrux):
                    return
                def innerLoop(j_idx: int) -> None:
                    nonlocal totalPairs
                    if j_idx == len(ktrux):
                        return
                    totalPairs += len(ktrux[i_idx]) * len(ktrux[j_idx])
                    innerLoop(j_idx + 1)
                innerLoop(i_idx + 1)
                sumPairs(i_idx + 1)

            sumPairs(0)

            return totalPairs

        def resultFill(idxx: int) -> None:
            if idxx == wwetaf:
                return
            cbvnep[idxx] = pairsCountThrough(idxx)
            resultFill(idxx + 1)

        resultFill(0)
        return cbvnep