from typing import List, Dict

class Solution:
    def minRunesToAdd(self, n: int, sgynAw: List[int], sresync: List[int]) -> int:
        # Helper function to build adjacency lists
        def BuildList(val: int, map_: Dict[int, List[int]]):
            if val not in map_:
                map_[val] = []
            map_[val].append(val)

        graph: Dict[int, List[int]] = {}
        reverseGraph: Dict[int, List[int]] = {}

        # Corrected BuildList following the pseudocode intent: attaching val to map_[e]
        def BuildList(e: int, val: int, map_: Dict[int, List[int]]):
            if e not in map_:
                map_[e] = []
            map_[e].append(val)

        # Add edges from sgynAw to sresync into graph and reverseGraph
        def addEdges(ix: int):
            if ix >= len(sgynAw):
                return
            startNode = sgynAw[ix]
            endNode = sresync[ix]
            BuildList(startNode, endNode, graph)
            BuildList(endNode, startNode, reverseGraph)
            addEdges(ix + 1)

        addEdges(0)

        indices = [-1] * n
        lows = [0] * n
        stackFlag = [False] * n
        workingStack: List[int] = []
        currentIndex = 0
        components: List[List[int]] = []

        def smaller(a: int, b: int) -> int:
            return a if a < b else b

        # Finding Strongly Connected Components using Tarjan's Algorithm
        def tarjan(cur: int):
            nonlocal currentIndex
            indices[cur] = currentIndex
            lows[cur] = currentIndex
            currentIndex += 1
            workingStack.append(cur)
            stackFlag[cur] = True

            def iterateNeighbors(pos: int):
                if pos >= len(graph.get(cur, [])):
                    return
                neigh = graph[cur][pos]
                if indices[neigh] == -1:
                    tarjan(neigh)
                    lows[cur] = smaller(lows[cur], lows[neigh])
                else:
                    if stackFlag[neigh]:
                        lows[cur] = smaller(lows[cur], indices[neigh])
                iterateNeighbors(pos + 1)

            iterateNeighbors(0)

            if lows[cur] == indices[cur]:
                memberList = []

                def peelStack():
                    topElem = workingStack.pop()
                    stackFlag[topElem] = False
                    memberList.append(topElem)
                    if topElem != cur:
                        peelStack()

                peelStack()
                components.append(memberList)

        def processIndices(pos: int):
            if pos == n:
                return
            if indices[pos] == -1:
                tarjan(pos)
            processIndices(pos + 1)

        processIndices(0)

        sccAtNode = [-1] * n
        hasCrystal = [False] * len(components)
        compCount = 0

        def assignComponents(ix: int):
            nonlocal compCount
            if ix == len(components):
                return
            cluster = components[ix]

            def markNodes(j: int):
                if j == len(cluster):
                    return
                nd = cluster[j]
                sccAtNode[nd] = compCount
                if nd in sresync:
                    hasCrystal[ix] = True
                markNodes(j + 1)

            markNodes(0)
            compCount += 1
            assignComponents(ix + 1)

        assignComponents(0)

        componentGraph: Dict[int, List[int]] = {}

        def addSccEdge(idx: int):
            if idx == len(sgynAw):
                return
            fromComp = sccAtNode[sgynAw[idx]]
            toComp = sccAtNode[sresync[idx]]
            if fromComp != toComp:
                if fromComp not in componentGraph:
                    componentGraph[fromComp] = []
                componentGraph[fromComp].append(toComp)
            addSccEdge(idx + 1)

        addSccEdge(0)

        incomingCount = [0] * len(components)

        def countIncoming(i: int):
            if i == len(components):
                return
            if i in componentGraph:
                def incrementIn(j: int):
                    if j == len(componentGraph[i]):
                        return
                    incomingCount[componentGraph[i][j]] += 1
                    incrementIn(j + 1)
                incrementIn(0)
            countIncoming(i + 1)

        countIncoming(0)

        neededTurns = 0

        def calcNeeded(k: int):
            nonlocal neededTurns
            if k == len(components):
                return
            if incomingCount[k] == 0 and not hasCrystal[k]:
                neededTurns += 1
            calcNeeded(k + 1)

        calcNeeded(0)

        return neededTurns