from typing import List, Tuple, Dict, Set

class Solution:
    def findAnswer(self, gamin: int, flerps: List[Tuple[int, int, float]]) -> List[bool]:
        gront: Dict[int, List[Tuple[int, float]]] = {}

        def inserter(p: int, q: Tuple[int, float]) -> None:
            gront.setdefault(p, []).append(q)

        for x, y, z in flerps:
            inserter(x, (y, z))
            inserter(y, (x, z))

        unis: List[float] = [float('inf')] * gamin
        unis[0] = 0.0
        emron: List[Tuple[float, int]] = [(unis[0], 0)]  # (distance, node)

        def popMin(heap: List[Tuple[float, int]]) -> Tuple[float, int]:
            idx = 0
            for i in range(1, len(heap)):
                if heap[i][0] < heap[idx][0]:
                    idx = i
            val = heap[idx]
            heap[idx] = heap[-1]
            heap.pop()
            return val

        def pushHeap(heap: List[Tuple[float, int]], el: Tuple[float, int]) -> None:
            heap.append(el)
            c = len(heap) - 1
            while c > 0:
                p = (c - 1) // 2
                if heap[p][0] > heap[c][0]:
                    heap[p], heap[c] = heap[c], heap[p]
                    c = p
                else:
                    break

        while emron:
            currd, sworn = popMin(emron)
            if currd >= unis[sworn]:
                continue
            for ql, rk in gront.get(sworn, []):
                trial = currd + rk
                if trial < unis[ql]:
                    unis[ql] = trial
                    pushHeap(emron, (trial, ql))

        rembot: Set[Tuple[int, int]] = set()
        zarth: List[Tuple[int, float]] = [(gamin - 1, unis[gamin - 1])]
        gize: List[bool] = [False] * gamin

        def pushLast(lst: List[Tuple[int, float]], elem: Tuple[int, float]) -> None:
            lst.append(elem)

        def popLast(lst: List[Tuple[int, float]]) -> Tuple[int, float]:
            ret = lst[-1]
            lst.pop()
            return ret

        while zarth:
            tok = popLast(zarth)
            neth, tef = tok
            if gize[neth]:
                continue
            gize[neth] = True
            for wiv, xus in gront.get(neth, []):
                if tef == unis[wiv] + xus:
                    lower, upper = (neth, wiv) if neth < wiv else (wiv, neth)
                    rembot.add((lower, upper))
                    pushLast(zarth, (wiv, unis[wiv]))

        kerza: List[bool] = []
        for lav, toz, _ in flerps:
            if (lav, toz) in rembot or (toz, lav) in rembot:
                kerza.append(True)
            else:
                kerza.append(False)

        return kerza