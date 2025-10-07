from collections import defaultdict
from typing import List, Set

class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: Set[int]) -> int:
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)

        for startNode, endNode in zip(flowFrom, flowTo):
            graph[startNode].append(endNode)
            reverse_graph[endNode].append(startNode)

        indices = [-1] * n
        lowLinks = [0] * n
        onStack = [False] * n
        stack = []
        currIndex = 0
        sccs = []

        def tarjan(node: int):
            nonlocal currIndex
            indices[node] = currIndex
            lowLinks[node] = currIndex
            currIndex += 1
            stack.append(node)
            onStack[node] = True

            for nbr in graph.get(node, []):
                if indices[nbr] == -1:
                    tarjan(nbr)
                    lowLinks[node] = min(lowLinks[node], lowLinks[nbr])
                elif onStack[nbr]:
                    lowLinks[node] = min(lowLinks[node], indices[nbr])

            if lowLinks[node] == indices[node]:
                component = []
                while True:
                    w = stack.pop()
                    onStack[w] = False
                    component.append(w)
                    if w == node:
                        break
                sccs.append(component)

        for i in range(n):
            if indices[i] == -1:
                tarjan(i)

        sccGraph = defaultdict(list)
        sccIndex = [-1] * n
        sccHasCrystal = [False] * len(sccs)
        sccCount = 0

        for idx, componentNodes in enumerate(sccs):
            for eachNode in componentNodes:
                sccIndex[eachNode] = idx
                if eachNode in crystals:
                    sccHasCrystal[idx] = True
            sccCount += 1

        for src, dst in zip(flowFrom, flowTo):
            srcScc = sccIndex[src]
            dstScc = sccIndex[dst]
            if srcScc != dstScc:
                sccGraph[srcScc].append(dstScc)

        inDegree = [0] * len(sccs)
        for srcScc, nbrs in sccGraph.items():
            for nxt in nbrs:
                inDegree[nxt] += 1

        additionalRunes = 0
        for idxScc in range(len(sccs)):
            if inDegree[idxScc] == 0 and not sccHasCrystal[idxScc]:
                additionalRunes += 1

        return additionalRunes