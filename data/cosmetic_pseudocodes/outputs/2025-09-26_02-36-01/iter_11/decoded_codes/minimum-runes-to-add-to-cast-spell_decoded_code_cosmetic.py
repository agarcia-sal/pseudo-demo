from collections import defaultdict
from typing import List

class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: List[int]) -> int:
        mappingAlpha = defaultdict(list)  # node -> list of neighbors
        mappingBeta = defaultdict(list)   # reverse edges

        def helperBuild():
            p = 0
            while p < len(flowFrom):
                keyX = flowFrom[p]
                keyY = flowTo[p]
                mappingAlpha[keyX].append(keyY)
                mappingBeta[keyY].append(keyX)
                p += 1

        helperBuild()

        identifiers = [-1] * n
        lowMarks = [0] * n
        activeFlags = [False] * n
        dataStack = []
        nextIndex = 0
        components = []

        # We use nonlocal to modify nextIndex inside nestedTarjan
        def nestedTarjan(currentNode):
            nonlocal nextIndex
            identifiers[currentNode] = nextIndex
            lowMarks[currentNode] = nextIndex
            nextIndex += 1
            dataStack.append(currentNode)
            activeFlags[currentNode] = True

            def loopAdjacents(pos):
                if pos >= len(mappingAlpha[currentNode]):
                    return
                neighborNode = mappingAlpha[currentNode][pos]
                if identifiers[neighborNode] == -1:
                    nestedTarjan(neighborNode)
                    lowMarks[currentNode] = min(lowMarks[currentNode], lowMarks[neighborNode])
                elif activeFlags[neighborNode]:
                    lowMarks[currentNode] = min(lowMarks[currentNode], identifiers[neighborNode])
                loopAdjacents(pos + 1)

            loopAdjacents(0)

            if lowMarks[currentNode] == identifiers[currentNode]:
                componentList = []

                def popStack():
                    val = dataStack.pop()
                    activeFlags[val] = False
                    componentList.append(val)
                    if val != currentNode:
                        popStack()

                popStack()
                components.append(componentList)

        def iterIndices(i):
            if i >= n:
                return
            if identifiers[i] == -1:
                nestedTarjan(i)
            iterIndices(i + 1)

        iterIndices(0)

        condensedGraph = defaultdict(list)
        assignSCC = [-1] * n
        haveCrystal = [False] * len(components)
        sccCounter = 0

        def assignLoop(idx):
            nonlocal sccCounter
            if idx >= len(components):
                return
            for nodeElement in components[idx]:
                assignSCC[nodeElement] = sccCounter
                if nodeElement in crystals:
                    haveCrystal[idx] = True
            sccCounter += 1
            assignLoop(idx + 1)

        assignLoop(0)

        def sccEdgesIterator(pos):
            if pos >= len(flowFrom):
                return
            sourceSCC = assignSCC[flowFrom[pos]]
            targetSCC = assignSCC[flowTo[pos]]
            if sourceSCC != targetSCC:
                condensedGraph[sourceSCC].append(targetSCC)
            sccEdgesIterator(pos + 1)

        sccEdgesIterator(0)

        inboundCount = [0] * len(components)

        def countInbounds(i):
            if i >= len(components):
                return
            for neighborNode in condensedGraph[i]:
                inboundCount[neighborNode] += 1
            countInbounds(i + 1)

        countInbounds(0)

        resultValue = 0

        def checkNoInbound(j):
            nonlocal resultValue
            if j >= len(components):
                return
            if inboundCount[j] == 0 and not haveCrystal[j]:
                resultValue += 1
            checkNoInbound(j + 1)

        checkNoInbound(0)

        return resultValue