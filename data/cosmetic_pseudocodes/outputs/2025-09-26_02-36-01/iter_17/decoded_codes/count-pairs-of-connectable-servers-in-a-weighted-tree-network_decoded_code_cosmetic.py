from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        adjacencyMap = defaultdict(list)

        def addEdge(a: int, b: int, w: int) -> None:
            adjacencyMap[a].append((b, w))

        # Build adjacency map; nodes assumed 0-based indexing
        for edge in edges:
            x, y, z = edge
            addEdge(x, y, z)
            addEdge(y, x, z)

        totalNodes = len(adjacencyMap)
        outputList = [0] * totalNodes

        def depthSearchRecursion(current: int, prev: int, distAccum: int, collected: List[int]) -> int:
            condCheck = (distAccum % signalSpeed) == 0
            if condCheck:
                collected.append(current)

            sumFound = 0
            connections = adjacencyMap[current]
            for nbr, wgt in connections:
                if nbr != prev:
                    sumFound += depthSearchRecursion(nbr, current, distAccum + wgt, collected)

            return sumFound + 1 if condCheck else sumFound

        def countPairsViaNode(center: int) -> int:
            collectedPaths = []
            neighborsList = adjacencyMap[center]
            for nbrNode, weightEdge in neighborsList:
                tempPath = []
                depthSearchRecursion(nbrNode, center, weightEdge, tempPath)
                collectedPaths.append(tempPath)

            pairCount = 0
            pLen = len(collectedPaths)
            for m1 in range(pLen):
                for m2 in range(m1 + 1, pLen):
                    sizeA = len(collectedPaths[m1])
                    sizeB = len(collectedPaths[m2])
                    pairCount += sizeA * sizeB
            return pairCount

        for nodeIndex in range(totalNodes):
            outputList[nodeIndex] = countPairsViaNode(nodeIndex)

        return outputList