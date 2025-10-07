from collections import defaultdict

class Solution:
    def minRunesToAdd(self, n, flowFrom, flowTo, crystals):
        adjList = defaultdict(list)
        revAdjList = defaultdict(list)

        idx = 0
        stackList = []
        discovered = [-1] * n
        lowLink = [0] * n
        inStack = [False] * n
        stronglyConnectedComponents = []

        for startNode, endNode in zip(flowFrom, flowTo):
            adjList[startNode].append(endNode)
            revAdjList[endNode].append(startNode)

        def tarjan(currentNode):
            nonlocal idx
            discovered[currentNode] = idx
            lowLink[currentNode] = idx
            idx += 1
            stackList.append(currentNode)
            inStack[currentNode] = True

            neighbors = adjList.get(currentNode, [])
            for nextNode in neighbors:
                if discovered[nextNode] == -1:
                    tarjan(nextNode)
                    if lowLink[nextNode] < lowLink[currentNode]:
                        lowLink[currentNode] = lowLink[nextNode]
                elif inStack[nextNode]:
                    if discovered[nextNode] < lowLink[currentNode]:
                        lowLink[currentNode] = discovered[nextNode]

            if lowLink[currentNode] == discovered[currentNode]:
                component = []
                while True:
                    popped = stackList.pop()
                    inStack[popped] = False
                    component.append(popped)
                    if popped == currentNode:
                        break
                stronglyConnectedComponents.append(component)

        for count in range(n):
            if discovered[count] == -1:
                tarjan(count)

        sccMapping = [-1] * n
        sccHasCrystal = [False] * len(stronglyConnectedComponents)
        derivedGraph = defaultdict(list)

        for sccIndexIter, comp in enumerate(stronglyConnectedComponents):
            for element in comp:
                sccMapping[element] = sccIndexIter
                if element in crystals:
                    sccHasCrystal[sccIndexIter] = True

        for nodeU, nodeV in zip(flowFrom, flowTo):
            sourceSCC = sccMapping[nodeU]
            targetSCC = sccMapping[nodeV]
            if sourceSCC != targetSCC:
                derivedGraph[sourceSCC].append(targetSCC)

        incomingDegree = [0] * len(stronglyConnectedComponents)
        for sccIdx in range(len(stronglyConnectedComponents)):
            adjNodes = derivedGraph.get(sccIdx, [])
            for adj in adjNodes:
                incomingDegree[adj] += 1

        neededRuns = 0
        for sccToCheck in range(len(stronglyConnectedComponents)):
            if incomingDegree[sccToCheck] == 0 and not sccHasCrystal[sccToCheck]:
                neededRuns += 1

        return neededRuns