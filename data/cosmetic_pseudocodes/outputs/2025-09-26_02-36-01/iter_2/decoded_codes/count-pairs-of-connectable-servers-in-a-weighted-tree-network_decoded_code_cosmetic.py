from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        adjacencyMap = defaultdict(list)
        index = 0
        while index < len(edges):
            firstNode, secondNode, weightVal = edges[index]
            adjacencyMap[firstNode].append((secondNode, weightVal))
            adjacencyMap[secondNode].append((firstNode, weightVal))
            index += 1

        totalNodes = len(adjacencyMap)
        pairsCountList = [0] * totalNodes

        def dfs(current, ancestor, accumulatedDistance, pathList):
            remainderVal = accumulatedDistance % signalSpeed
            if remainderVal == 0:
                pathList.append(current)
            subCount = 0
            for neighborNode, edgeWeight in adjacencyMap[current]:
                if neighborNode != ancestor:
                    subCount += dfs(neighborNode, current, accumulatedDistance + edgeWeight, pathList)
            return subCount + 1 if remainderVal == 0 else subCount

        def count_pairs_through_c(node_c):
            collectionPaths = []
            for neighborNode, edgeWeight in adjacencyMap[node_c]:
                currentPath = []
                dfs(neighborNode, node_c, edgeWeight, currentPath)
                collectionPaths.append(currentPath)
            aggregatePairs = 0
            for leftIdx in range(len(collectionPaths) - 1):
                leftLength = len(collectionPaths[leftIdx])
                for rightIdx in range(leftIdx + 1, len(collectionPaths)):
                    rightLength = len(collectionPaths[rightIdx])
                    aggregatePairs += leftLength * rightLength
            return aggregatePairs

        for counter in range(totalNodes):
            pairsCountList[counter] = count_pairs_through_c(counter)

        return pairsCountList