from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def dfs(currentNode: int, previousNode: int, distances: List[int]) -> None:
            for neighbor in g[currentNode]:
                if neighbor != previousNode:
                    distances[neighbor] = distances[currentNode] + 1
                    dfs(neighbor, currentNode, distances)

        count = len(edges) + 1
        g = [[] for _ in range(count)]
        for fromNode, toNode in edges:
            g[fromNode].append(toNode)
            g[toNode].append(fromNode)

        distancesOne = [-1] * count
        distancesOne[0] = 0
        dfs(0, -1, distancesOne)
        maxPos = max(range(count), key=lambda i: distancesOne[i])
        a = maxPos

        distancesTwo = [-1] * count
        distancesTwo[a] = 0
        dfs(a, -1, distancesTwo)
        maxPlace = max(range(count), key=lambda i: distancesTwo[i])
        b = maxPlace

        distancesThree = [-1] * count
        distancesThree[b] = 0
        dfs(b, -1, distancesThree)

        finalList = []
        for posIndex in range(count):
            valOne = distancesTwo[posIndex]
            valTwo = distancesThree[posIndex]
            if valOne > valTwo:
                finalList.append(a)
            else:
                finalList.append(b)

        return finalList