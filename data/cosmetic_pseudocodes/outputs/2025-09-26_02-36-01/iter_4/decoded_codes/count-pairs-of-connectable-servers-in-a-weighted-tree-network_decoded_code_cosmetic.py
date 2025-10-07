from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        adjacencyMap = defaultdict(list)
        index = 0
        while index < len(edges):
            currentEdge = edges[index]
            source = currentEdge[0]
            target = currentEdge[1]
            delay = currentEdge[2]
            adjacencyMap[source].append([target, delay])
            adjacencyMap[target].append([source, delay])
            index += 1

        nodeCount = len(adjacencyMap)
        answers = [0] * nodeCount

        def dfs(currentNode, prevNode, accumulatedDistance, accumulatorPath):
            modCheck = accumulatedDistance % signalSpeed
            if modCheck == 0:
                accumulatorPath.append(currentNode)

            subtreeSum = 0
            edgeIndex = 0
            while edgeIndex < len(adjacencyMap[currentNode]):
                adjacentPair = adjacencyMap[currentNode][edgeIndex]
                neighborNode = adjacentPair[0]
                edgeWeight = adjacentPair[1]
                if neighborNode != prevNode:
                    recursiveCount = dfs(neighborNode, currentNode, accumulatedDistance + edgeWeight, accumulatorPath)
                    subtreeSum += recursiveCount
                edgeIndex += 1

            if accumulatedDistance % signalSpeed == 0:
                return subtreeSum + 1
            else:
                return subtreeSum

        def count_pairs_through_c(c):
            collectedPaths = []
            neighborIndex = 0
            while neighborIndex < len(adjacencyMap[c]):
                neighborInfo = adjacencyMap[c][neighborIndex]
                pathList = []
                dfs(neighborInfo[0], c, neighborInfo[1], pathList)
                collectedPaths.append(pathList)
                neighborIndex += 1

            pairSum = 0
            outerIndex = 0
            while outerIndex < len(collectedPaths) - 1:
                innerIndex = outerIndex + 1
                while innerIndex < len(collectedPaths):
                    countA = len(collectedPaths[outerIndex])
                    countB = len(collectedPaths[innerIndex])
                    pairSum += countA * countB
                    innerIndex += 1
                outerIndex += 1

            return pairSum

        currentNode = 0
        while currentNode < nodeCount:
            answers[currentNode] = count_pairs_through_c(currentNode)
            currentNode += 1

        return answers