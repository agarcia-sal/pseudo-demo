from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        n = len(graph)
        result = [0] * n

        def dfs(currentNode, parentNode, dist, collectedNodes):
            if dist % signalSpeed == 0:
                collectedNodes.append(currentNode)
            subtreeCount = 0
            for adjacentNode, edgeWeight in graph[currentNode]:
                if adjacentNode != parentNode:
                    subtreeCount += dfs(adjacentNode, currentNode, dist + edgeWeight, collectedNodes)
            if dist % signalSpeed == 0:
                return subtreeCount + 1
            else:
                return subtreeCount

        def count_pairs_through_c(c):
            pathsList = []
            for neighbor, weight in graph[c]:
                collectedPath = []
                dfs(neighbor, c, weight, collectedPath)
                pathsList.append(collectedPath)
            totalPairs = 0
            length = len(pathsList)
            for i in range(length - 1):
                for j in range(i + 1, length):
                    totalPairs += len(pathsList[i]) * len(pathsList[j])
            return totalPairs

        for nodeIndex in range(n):
            result[nodeIndex] = count_pairs_through_c(nodeIndex)

        return result