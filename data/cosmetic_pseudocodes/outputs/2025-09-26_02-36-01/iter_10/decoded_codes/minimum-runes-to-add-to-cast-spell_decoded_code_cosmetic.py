from collections import defaultdict
from typing import List, Set

class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: Set[int]) -> int:
        initialMapA = defaultdict(list)  # mapping from int to list of ints
        initialMapB = defaultdict(list)  # mapping from int to list of ints

        def fillGraphs():
            def fillLoop(ix):
                if ix >= n:
                    return
                keyA = flowFrom[ix]
                keyB = flowTo[ix]
                initialMapA[keyA].append(keyB)
                initialMapB[keyB].append(keyA)
                fillLoop(ix + 1)
            fillLoop(0)
        fillGraphs()

        idcs = [-1] * n
        lowL = [0] * n
        onStk = [False] * n
        stk = []
        currentIndex = 0
        components = []

        def executeTarjan(point):
            nonlocal currentIndex
            idcs[point] = currentIndex
            lowL[point] = currentIndex
            currentIndex += 1
            stk.append(point)
            onStk[point] = True

            def recurNeighbors(j):
                if j >= len(initialMapA[point]):
                    return
                nb = initialMapA[point][j]
                if idcs[nb] == -1:
                    executeTarjan(nb)
                    if lowL[nb] < lowL[point]:
                        lowL[point] = lowL[nb]
                elif onStk[nb]:
                    if idcs[nb] < lowL[point]:
                        lowL[point] = idcs[nb]
                recurNeighbors(j + 1)
            recurNeighbors(0)

            if lowL[point] == idcs[point]:
                curScc = []
                def popStack():
                    w = stk.pop()
                    onStk[w] = False
                    curScc.append(w)
                    if w != point:
                        popStack()
                popStack()
                components.append(curScc)

        def iterateIndices(k):
            if k >= n:
                return
            if idcs[k] == -1:
                executeTarjan(k)
            iterateIndices(k + 1)
        iterateIndices(0)

        condGraph = defaultdict(list)  # mapping int -> list of ints (component graph)
        belonging = [-1] * n
        hasCrys = [False] * len(components)
        compCount = 0

        def assignComponents(p):
            nonlocal compCount
            if p >= len(components):
                return
            cList = components[p]
            def assignNodes(y):
                if y >= len(cList):
                    return
                node = cList[y]
                belonging[node] = compCount
                if node in crystals:
                    hasCrys[p] = True
                assignNodes(y + 1)
            assignNodes(0)
            compCount += 1
            assignComponents(p + 1)
        assignComponents(0)

        def buildCondGraph(z):
            if z >= n:
                return
            fromScc = belonging[flowFrom[z]]
            toScc = belonging[flowTo[z]]
            if fromScc != toScc:
                condGraph[fromScc].append(toScc)
            buildCondGraph(z + 1)
        buildCondGraph(0)

        inDegree = [0] * len(components)

        def countIns(r):
            if r >= len(components):
                return
            if r in condGraph:
                def incDegrees(m):
                    if m >= len(condGraph[r]):
                        return
                    target = condGraph[r][m]
                    inDegree[target] += 1
                    incDegrees(m + 1)
                incDegrees(0)
            countIns(r + 1)
        countIns(0)

        needed = 0

        def evaluateAdditions(s):
            nonlocal needed
            if s >= len(components):
                return
            conditionA = (inDegree[s] == 0)
            conditionB = (not hasCrys[s])
            if conditionA and conditionB:
                needed += 1
            evaluateAdditions(s + 1)
        evaluateAdditions(0)

        return needed