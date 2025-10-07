from collections import defaultdict
from typing import List

class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: List[int]) -> int:
        adjMap = defaultdict(list)
        revAdjMap = defaultdict(list)

        for x, y in zip(flowFrom, flowTo):
            adjMap[x].append(y)
            revAdjMap[y].append(x)

        idxCounter = 0
        nodeStack = []
        hasStackFlag = [False] * n
        discoveryTime = [-1] * n
        lowTime = [0] * n
        sccGroups = []

        def strongConnect(v: int):
            nonlocal idxCounter
            discoveryTime[v] = idxCounter
            lowTime[v] = idxCounter
            idxCounter += 1
            nodeStack.append(v)
            hasStackFlag[v] = True

            neighbors = adjMap[v] if v in adjMap else []
            for node_u in neighbors:
                if discoveryTime[node_u] == -1:
                    strongConnect(node_u)
                    lowTime[v] = min(lowTime[v], lowTime[node_u])
                elif hasStackFlag[node_u]:
                    lowTime[v] = min(lowTime[v], discoveryTime[node_u])

            if lowTime[v] == discoveryTime[v]:
                currentSCC = []
                while True:
                    poppedNode = nodeStack.pop()
                    hasStackFlag[poppedNode] = False
                    currentSCC.append(poppedNode)
                    if poppedNode == v:
                        break
                sccGroups.append(currentSCC)

        for vertex in range(n):
            if discoveryTime[vertex] == -1:
                strongConnect(vertex)

        sccMapping = [-1] * n
        sccHasCrystal = [False] * len(sccGroups)
        sccGraph = defaultdict(list)

        crystals_set = set(crystals)
        for index, group in enumerate(sccGroups):
            for node in group:
                sccMapping[node] = index
                if node in crystals_set:
                    sccHasCrystal[index] = True

        for edgeStart, edgeEnd in zip(flowFrom, flowTo):
            startGroup = sccMapping[edgeStart]
            endGroup = sccMapping[edgeEnd]
            if startGroup != endGroup:
                sccGraph[startGroup].append(endGroup)

        inboundEdgesCount = [0] * len(sccGroups)
        for group in range(len(sccGroups)):
            adjacents = sccGraph[group] if group in sccGraph else []
            for adjGroup in adjacents:
                inboundEdgesCount[adjGroup] += 1

        requiredAdditions = 0
        for sc in range(len(sccGroups)):
            if inboundEdgesCount[sc] == 0 and not sccHasCrystal[sc]:
                requiredAdditions += 1

        return requiredAdditions