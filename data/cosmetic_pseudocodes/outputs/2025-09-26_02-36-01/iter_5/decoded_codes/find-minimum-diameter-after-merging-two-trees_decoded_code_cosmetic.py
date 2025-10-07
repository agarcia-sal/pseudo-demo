from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        lengthGraph = len(graph)
        visitedFlags = [False] * lengthGraph

        def bfsHelper(queueContainer, currentFarthestNode, currentMaxDist):
            if len(queueContainer) == 0:
                return currentFarthestNode, currentMaxDist

            currentEntry = queueContainer.popleft()
            currentNode, currentDistance = currentEntry[0], currentEntry[1]

            if currentDistance > currentMaxDist:
                currentMaxDist = currentDistance
                currentFarthestNode = currentNode

            def processNeighbors(neighborList, index, totalLength):
                if index == totalLength:
                    return
                neighborNode = neighborList[index]
                if not visitedFlags[neighborNode]:
                    visitedFlags[neighborNode] = True
                    queueContainer.append([neighborNode, currentDistance + 1])
                processNeighbors(neighborList, index + 1, totalLength)

            processNeighbors(graph[currentNode], 0, len(graph[currentNode]))
            return bfsHelper(queueContainer, currentFarthestNode, currentMaxDist)

        visitedFlags[start] = True
        initialQueue = deque()
        initialQueue.append([start, 0])

        resultFarthestNode, resultMaxDistance = bfsHelper(initialQueue, start, 0)
        return resultFarthestNode, resultMaxDistance

    def tree_diameter(self, graph):
        zeroValue = 0
        firstNode = zeroValue
        nodeFarthest, _tempUnused = self.bfs(graph, firstNode)
        _anotherUnused, diameterLength = self.bfs(graph, nodeFarthest)
        return diameterLength

    def maximum_path_length_from_node(self, graph, startNode):
        lengthGraph = len(graph)
        visitedNodes = [False] * lengthGraph

        def maxPathHelper(queueArr, currentMax):
            if len(queueArr) == 0:
                return currentMax

            frontElement = queueArr.popleft()
            currentVertex, currentDistance = frontElement[0], frontElement[1]

            if currentDistance > currentMax:
                currentMax = currentDistance

            def processNeighborsRec(neighborsList, pos, total):
                if pos == total:
                    return
                neighborVer = neighborsList[pos]
                if not visitedNodes[neighborVer]:
                    visitedNodes[neighborVer] = True
                    queueArr.append([neighborVer, currentDistance + 1])
                processNeighborsRec(neighborsList, pos + 1, total)

            processNeighborsRec(graph[currentVertex], 0, len(graph[currentVertex]))
            return maxPathHelper(queueArr, currentMax)

        visitedNodes[startNode] = True
        initialQueue = deque()
        initialQueue.append([startNode, 0])

        maxDistanceFound = maxPathHelper(initialQueue, 0)
        return maxDistanceFound

    def minimumDiameterAfterMerge(self, edgesSet1, edgesSet2):
        lengthN = len(edgesSet1) + 1
        lengthM = len(edgesSet2) + 1

        graphStructure1 = [[] for _ in range(lengthN)]
        graphStructure2 = [[] for _ in range(lengthM)]

        def buildGraph(graphData, edgesList):
            def buildGraphHelper(pos):
                if pos == len(edgesList):
                    return
                edgeTuple = edgesList[pos]
                fromNode, toNode = edgeTuple[0], edgeTuple[1]
                graphData[fromNode].append(toNode)
                graphData[toNode].append(fromNode)
                buildGraphHelper(pos + 1)
            buildGraphHelper(0)

        buildGraph(graphStructure1, edgesSet1)
        buildGraph(graphStructure2, edgesSet2)

        diameterGraph1 = self.tree_diameter(graphStructure1)
        diameterGraph2 = self.tree_diameter(graphStructure2)

        longestPathsGraph1 = []
        iteratorSort1 = 0
        while iteratorSort1 < lengthN:
            longestPathsGraph1.append(self.maximum_path_length_from_node(graphStructure1, iteratorSort1))
            iteratorSort1 += 1

        longestPathsGraph2 = []
        iteratorSort2 = 0
        while iteratorSort2 < lengthM:
            longestPathsGraph2.append(self.maximum_path_length_from_node(graphStructure2, iteratorSort2))
            iteratorSort2 += 1

        minimumDiameter = inf

        outerIdx = 0
        while outerIdx < lengthN:
            innerIdx = 0
            while innerIdx < lengthM:
                candidateDiameter = diameterGraph1
                if diameterGraph2 > candidateDiameter:
                    candidateDiameter = diameterGraph2

                pathSum = longestPathsGraph1[outerIdx] + longestPathsGraph2[innerIdx] + 1
                if pathSum > candidateDiameter:
                    candidateDiameter = pathSum

                if candidateDiameter < minimumDiameter:
                    minimumDiameter = candidateDiameter

                innerIdx += 1
            outerIdx += 1

        return minimumDiameter