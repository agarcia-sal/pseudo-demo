from collections import defaultdict

class Solution:
    def minRunesToAdd(self, count: int, totalFrom: list[int], totalTo: list[int], gems: set[int]) -> int:
        def buildAdjacencyMap(asFrom: list[int], asTo: list[int]) -> dict[int, list[int]]:
            mapping = defaultdict(list)
            def iterator(i: int):
                if i == len(asFrom):
                    return
                startNode = asFrom[i]
                endNode = asTo[i]
                mapping[startNode].append(endNode)
                iterator(i + 1)
            iterator(0)
            return mapping

        forwardEdges = buildAdjacencyMap(totalFrom, totalTo)
        backwardEdges = buildAdjacencyMap(totalTo, totalFrom)

        indicesList = [-1] * count
        lowLinkList = [0] * count
        inStackStatus = [False] * count
        nodeStack = []
        currentIx = 0
        stronglyConnectedComponents = []

        # Tarjan's algorithm to find strongly connected components (SCCs)
        def exploreTarjan(currentNode: int):
            nonlocal currentIx
            indicesList[currentNode] = currentIx
            lowLinkList[currentNode] = currentIx
            currentIx += 1
            nodeStack.append(currentNode)
            inStackStatus[currentNode] = True

            for adjacentNode in forwardEdges.get(currentNode, []):
                if indicesList[adjacentNode] == -1:
                    exploreTarjan(adjacentNode)
                    lowLinkList[currentNode] = min(lowLinkList[currentNode], lowLinkList[adjacentNode])
                elif inStackStatus[adjacentNode]:
                    lowLinkList[currentNode] = min(lowLinkList[currentNode], indicesList[adjacentNode])

            if lowLinkList[currentNode] == indicesList[currentNode]:
                componentNodes = []
                while True:
                    lastAddedNode = nodeStack.pop()
                    inStackStatus[lastAddedNode] = False
                    componentNodes.append(lastAddedNode)
                    if lastAddedNode == currentNode:
                        break
                stronglyConnectedComponents.append(componentNodes)

        def doTarjanOnAllNodes(i: int):
            if i == count:
                return
            if indicesList[i] == -1:
                exploreTarjan(i)
            doTarjanOnAllNodes(i + 1)
        doTarjanOnAllNodes(0)

        condGraph = defaultdict(list)
        nodeToComponent = [-1] * count
        hasGemInComponent = [False] * len(stronglyConnectedComponents)
        componentCounter = 0

        def assignComponentFlags(j: int):
            nonlocal componentCounter
            if j == len(stronglyConnectedComponents):
                return
            currentComponent = stronglyConnectedComponents[j]
            for elementNode in currentComponent:
                nodeToComponent[elementNode] = componentCounter
                if elementNode in gems:
                    hasGemInComponent[j] = True
            componentCounter += 1
            assignComponentFlags(j + 1)
        assignComponentFlags(0)

        def addEdgesBetweenComponents(k: int):
            if k == len(totalFrom):
                return
            startComp = nodeToComponent[totalFrom[k]]
            endComp = nodeToComponent[totalTo[k]]
            if startComp != endComp:
                condGraph[startComp].append(endComp)
            addEdgesBetweenComponents(k + 1)
        addEdgesBetweenComponents(0)

        inDegreeCounts = [0] * len(stronglyConnectedComponents)

        def computeInDegrees(m: int):
            if m == len(stronglyConnectedComponents):
                return
            neighborsList = condGraph.get(m, [])
            def incrementNeighborDegrees(p: int):
                if p == len(neighborsList):
                    return
                inDegreeCounts[neighborsList[p]] += 1
                incrementNeighborDegrees(p + 1)
            incrementNeighborDegrees(0)
            computeInDegrees(m + 1)
        computeInDegrees(0)

        requiredAdds = 0
        def countComponentsWithoutIncoming(q: int):
            nonlocal requiredAdds
            if q == len(stronglyConnectedComponents):
                return
            if inDegreeCounts[q] == 0 and not hasGemInComponent[q]:
                requiredAdds += 1
            countComponentsWithoutIncoming(q + 1)
        countComponentsWithoutIncoming(0)

        return requiredAdds