from collections import defaultdict

class Solution:
    def minRunesToAdd(self, n, flowFrom, flowTo, crystals):
        graphMap = defaultdict(list)
        reverseMap = defaultdict(list)

        def populateGraphs():
            posA = 0
            while True:
                if posA >= len(flowFrom):
                    break
                valR = flowFrom[posA]
                valS = flowTo[posA]
                graphMap[valR].append(valS)
                reverseMap[valS].append(valR)
                posA += 1

        indices = [-1] * n
        lowLinks = [0] * n
        onStack = [False] * n
        stack = []
        idxCounter = 0
        sccs = []

        def tarjanRec(node):
            nonlocal idxCounter
            indices[node] = idxCounter
            lowLinks[node] = idxCounter
            idxCounter += 1
            stack.append(node)
            onStack[node] = True

            neighbors = graphMap.get(node, [])
            for nbr in neighbors:
                if indices[nbr] < 0:
                    tarjanRec(nbr)
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

        def initializeIndices():
            for i in range(n):
                indices[i] = -1
                lowLinks[i] = 0
                onStack[i] = False

        initializeIndices()
        populateGraphs()

        for i in range(n):
            if indices[i] < 0:
                tarjanRec(i)

        sccGraph = defaultdict(list)
        sccIndex = [-1] * n
        sccHasCrystal = [False] * len(sccs)
        currScc = 0
        outerIdx = 0

        while outerIdx < len(sccs):
            currComponent = sccs[outerIdx]
            inner = 0
            while inner < len(currComponent):
                nd = currComponent[inner]
                sccIndex[nd] = currScc
                if nd in crystals:
                    sccHasCrystal[outerIdx] = True
                inner += 1
            currScc += 1
            outerIdx += 1

        pos = 0
        while pos < len(flowFrom):
            valU = flowFrom[pos]
            valV = flowTo[pos]
            idU = sccIndex[valU]
            idV = sccIndex[valV]
            if idU != idV:
                if idV not in sccGraph[idU]:
                    sccGraph[idU].append(idV)
            pos += 1

        indegreeList = [0] * len(sccs)
        si = 0
        while si < len(sccs):
            adjList = sccGraph.get(si, [])
            pi = 0
            while pi < len(adjList):
                neighb = adjList[pi]
                indegreeList[neighb] += 1
                pi += 1
            si += 1

        additions = 0
        sj = 0
        while sj < len(sccs):
            if indegreeList[sj] == 0 and sccHasCrystal[sj] is False:
                additions += 1
            sj += 1

        return additions