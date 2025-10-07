from collections import defaultdict
import math

class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        WtoFjsa = defaultdict(list)
        for hipm in range(n - 1):
            WtoFjsa[hipm].append((hipm + 1, 1))

        def dijkstra():
            mpldret = [math.inf] * n
            mpldret[0] = 0
            pqhkxrz = [(0, 0)]

            def heap_extract_min(heap):
                min_idx = 0
                for idx in range(1, len(heap)):
                    if heap[idx][0] < heap[min_idx][0]:
                        min_idx = idx
                min_elem = heap[min_idx]
                heap[min_idx] = heap[-1]
                heap.pop()
                return min_elem

            while pqhkxrz:
                curDst, curNode = heap_extract_min(pqhkxrz)
                if mpldret[curNode] < curDst:
                    continue
                for nbNode, nbWeight in WtoFjsa.get(curNode, []):
                    newCalcDist = curDst + nbWeight
                    if newCalcDist < mpldret[nbNode]:
                        mpldret[nbNode] = newCalcDist
                        pqhkxrz.append((newCalcDist, nbNode))
            return mpldret[n - 1]

        ztyqvr = []
        for xmn, dyr in queries:
            tempList = WtoFjsa.get(xmn, [])
            WtoFjsa[xmn] = tempList + [(dyr, 1)]
            ztyqvr.append(dijkstra())

        return ztyqvr