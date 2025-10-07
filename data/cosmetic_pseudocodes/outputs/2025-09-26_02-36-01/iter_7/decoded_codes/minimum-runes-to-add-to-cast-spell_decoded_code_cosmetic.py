from collections import defaultdict
from typing import List

class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: List[int]) -> int:
        g = defaultdict(list)
        revG = defaultdict(list)

        for i in range(len(flowFrom)):
            fromNode = flowFrom[i]
            toNode = flowTo[i]
            g[fromNode].append(toNode)
            revG[toNode].append(fromNode)

        idxs = [-1] * n
        lowL = [0] * n
        stk = []
        onStk = [False] * n
        curInd = 0
        sccList = []

        def tarjan(currNode):
            nonlocal curInd
            idxs[currNode] = curInd
            lowL[currNode] = curInd
            curInd += 1
            stk.append(currNode)
            onStk[currNode] = True

            for nb in g[currNode]:
                if idxs[nb] == -1:
                    tarjan(nb)
                    lowL[currNode] = min(lowL[currNode], lowL[nb])
                elif onStk[nb]:
                    lowL[currNode] = min(lowL[currNode], idxs[nb])

            if lowL[currNode] == idxs[currNode]:
                component = []
                while True:
                    w = stk.pop()
                    onStk[w] = False
                    component.append(w)
                    if w == currNode:
                        break
                sccList.append(component)

        for z in range(n):
            if idxs[z] == -1:
                tarjan(z)

        sccG = defaultdict(list)
        sccIDs = [-1] * n
        hasCrystal = [False] * len(sccList)
        countSCC = 0

        for idxSCC, grp in enumerate(sccList):
            for node in grp:
                sccIDs[node] = countSCC
                if node in crystals:
                    hasCrystal[countSCC] = True
            countSCC += 1

        for i in range(len(flowFrom)):
            uID = sccIDs[flowFrom[i]]
            vID = sccIDs[flowTo[i]]
            if uID != vID:
                sccG[uID].append(vID)

        indeg = [0] * len(sccList)
        for m in range(len(sccList)):
            if m in sccG:
                for neighbor in sccG[m]:
                    indeg[neighbor] += 1

        addedRunes = 0
        for s in range(len(sccList)):
            if indeg[s] == 0 and not hasCrystal[s]:
                addedRunes += 1

        return addedRunes