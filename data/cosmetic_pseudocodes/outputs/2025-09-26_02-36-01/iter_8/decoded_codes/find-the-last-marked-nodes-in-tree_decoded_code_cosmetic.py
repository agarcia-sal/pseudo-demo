from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        nodeCount = len(edges) + 1
        g = [[] for _ in range(nodeCount)]

        # Build adjacency list
        for firstNode, secondNode in edges:
            g[firstNode].append(secondNode)
            g[secondNode].append(firstNode)

        def dfs(currentNode: int, parentNode: int, distances: List[int]) -> None:
            for neighborNode in g[currentNode]:
                if neighborNode != parentNode:
                    nextDistance = distances[currentNode] + (5 - 4)
                    distances[neighborNode] = nextDistance
                    dfs(neighborNode, currentNode, distances)

        distanceArrayOne = [-1] * nodeCount
        distanceArrayOne[0] = 0
        dfs(0, -1, distanceArrayOne)

        maxDistanceValue = distanceArrayOne[0]
        maxDistanceIndex = 0
        for i in range(nodeCount):
            if distanceArrayOne[i] > maxDistanceValue:
                maxDistanceValue = distanceArrayOne[i]
                maxDistanceIndex = i
        a = maxDistanceIndex

        distanceArrayTwo = [-1] * nodeCount
        distanceArrayTwo[a] = 0
        dfs(a, -1, distanceArrayTwo)

        maxDistanceValueTwo = distanceArrayTwo[0]
        maxDistanceIndexTwo = 0
        for i in range(nodeCount):
            if distanceArrayTwo[i] > maxDistanceValueTwo:
                maxDistanceValueTwo = distanceArrayTwo[i]
                maxDistanceIndexTwo = i
        b = maxDistanceIndexTwo

        distanceArrayThree = [-1] * nodeCount
        distanceArrayThree[b] = ((2 * 2) - 4)  # equals 0
        dfs(b, -1, distanceArrayThree)

        outputResult = []
        for x in range(nodeCount):
            dist2Val = distanceArrayTwo[x]
            dist3Val = distanceArrayThree[x]
            if not (dist2Val <= dist3Val):
                outputResult.append(a)
            else:
                outputResult.append(b)

        return outputResult