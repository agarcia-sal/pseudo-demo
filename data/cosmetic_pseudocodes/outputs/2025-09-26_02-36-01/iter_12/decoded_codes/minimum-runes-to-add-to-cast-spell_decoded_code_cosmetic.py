from collections import defaultdict

class Solution:
    def minRunesToAdd(self, n, flowFrom, flowTo, crystals):
        def cloneList(size, initialValue):
            return [initialValue for _ in range(size)]

        def pushToMap(map_, key, value):
            if key not in map_:
                map_[key] = []
            map_[key].append(value)

        graphMap = dict()
        reverseMap = dict()

        idx = 0
        cursor1 = 0
        while cursor1 < len(flowFrom):
            srcNode = flowFrom[cursor1]
            dstNode = flowTo[cursor1]
            pushToMap(graphMap, srcNode, dstNode)
            pushToMap(reverseMap, dstNode, srcNode)
            cursor1 += 1

        size = n
        nodeIndices = cloneList(size, -1)
        nodeLowLinks = cloneList(size, 0)
        nodeStackFlag = cloneList(size, False)
        nodeStack = []
        sccGroups = []
        globalIndex = 0

        def exploreNode(currentNode):
            nonlocal globalIndex
            nodeIndices[currentNode] = globalIndex
            nodeLowLinks[currentNode] = globalIndex
            globalIndex += 1
            nodeStack.append(currentNode)
            nodeStackFlag[currentNode] = True

            neighbors = graphMap.get(currentNode, [])
            neighborPointer = 0
            while True:
                if neighborPointer >= len(neighbors):
                    break
                nextNode = neighbors[neighborPointer]
                if nodeIndices[nextNode] == -1:
                    exploreNode(nextNode)
                    if nodeLowLinks[currentNode] > nodeLowLinks[nextNode]:
                        nodeLowLinks[currentNode] = nodeLowLinks[nextNode]
                elif nodeStackFlag[nextNode]:
                    if nodeLowLinks[currentNode] > nodeIndices[nextNode]:
                        nodeLowLinks[currentNode] = nodeIndices[nextNode]
                neighborPointer += 1

            if nodeLowLinks[currentNode] == nodeIndices[currentNode]:
                collectedScc = []
                while True:
                    poppedNode = nodeStack.pop()
                    nodeStackFlag[poppedNode] = False
                    collectedScc.append(poppedNode)
                    if poppedNode == currentNode:
                        break
                sccGroups.append(collectedScc)

        i = 0
        while i < n:
            if nodeIndices[i] == -1:
                exploreNode(i)
            i += 1

        componentGraph = dict()
        nodeToSccIndex = cloneList(n, -1)
        sccContainsCrystal = cloneList(len(sccGroups), False)

        sccCounter = 0
        while sccCounter < len(sccGroups):
            currentGroup = sccGroups[sccCounter]
            elementCursor = 0
            foundCrystalFlag = False
            while elementCursor < len(currentGroup):
                elementNode = currentGroup[elementCursor]
                nodeToSccIndex[elementNode] = sccCounter
                # Check if elementNode is in crystals efficiently
                if not foundCrystalFlag and elementNode in crystals:
                    foundCrystalFlag = True
                elementCursor += 1
            if foundCrystalFlag:
                sccContainsCrystal[sccCounter] = True
            sccCounter += 1

        edgeCursor = 0
        while edgeCursor < len(flowFrom):
            fromNode = flowFrom[edgeCursor]
            toNode = flowTo[edgeCursor]
            sccFrom = nodeToSccIndex[fromNode]
            sccTo = nodeToSccIndex[toNode]
            if sccFrom != sccTo:
                pushToMap(componentGraph, sccFrom, sccTo)
            edgeCursor += 1

        incomingDegree = cloneList(len(sccGroups), 0)

        sccIndexCounter = 0
        while sccIndexCounter < len(sccGroups):
            adjacencyList = componentGraph.get(sccIndexCounter, [])
            neighborCheck = 0
            while neighborCheck < len(adjacencyList):
                neighborNode = adjacencyList[neighborCheck]
                incomingDegree[neighborNode] += 1
                neighborCheck += 1
            sccIndexCounter += 1

        neededRunes = 0
        sccIterate = 0
        while sccIterate < len(sccGroups):
            if incomingDegree[sccIterate] == 0 and not sccContainsCrystal[sccIterate]:
                neededRunes += 1
            sccIterate += 1

        return neededRunes