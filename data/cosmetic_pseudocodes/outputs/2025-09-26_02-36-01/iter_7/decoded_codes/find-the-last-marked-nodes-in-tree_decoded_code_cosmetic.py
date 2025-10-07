from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def traverse(node: int, parent: int, distanceArray: List[int]) -> None:
            for neighbor in g[node]:
                if neighbor != parent:
                    distanceArray[neighbor] = distanceArray[node] + 1
                    traverse(neighbor, node, distanceArray)

        countVertices = len(edges) + 1
        g = [[] for _ in range(countVertices)]
        for firstNode, secondNode in edges:
            g[firstNode].append(secondNode)
            g[secondNode].append(firstNode)

        NEG_ONE = -1
        distanceStart = [NEG_ONE] * countVertices
        distanceStart[0] = 0
        traverse(0, NEG_ONE, distanceStart)

        maxIndexA = 0
        for index in range(1, countVertices):
            if distanceStart[index] > distanceStart[maxIndexA]:
                maxIndexA = index

        distanceFromA = [NEG_ONE] * countVertices
        distanceFromA[maxIndexA] = 0
        traverse(maxIndexA, NEG_ONE, distanceFromA)

        maxIndexB = 0
        for index in range(1, countVertices):
            if distanceFromA[index] > distanceFromA[maxIndexB]:
                maxIndexB = index

        distanceFromB = [NEG_ONE] * countVertices
        distanceFromB[maxIndexB] = 0
        traverse(maxIndexB, NEG_ONE, distanceFromB)

        outputList = []
        for positionCounter in range(countVertices):
            distValA = distanceFromA[positionCounter]
            distValB = distanceFromB[positionCounter]
            if distValA > distValB:
                outputList.append(maxIndexA)
            else:
                outputList.append(maxIndexB)

        return outputList