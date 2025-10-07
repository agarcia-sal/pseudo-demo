from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        adjacencyMap = defaultdict(list)

        def addEdge(a: int, b: int) -> None:
            adjacencyMap[a].append(b)
            adjacencyMap[b].append(a)

        for edgePair in edges:
            addEdge(edgePair[0], edgePair[1])

        maxSize = 1

        def traverseTree(current: int, prev: int) -> int:
            nonlocal maxSize
            totalSameColor = 1
            isUniform = True

            def processNeighbor(idx: int) -> None:
                nonlocal totalSameColor, isUniform
                if idx >= len(adjacencyMap[current]):
                    return

                neighborNode = adjacencyMap[current][idx]

                if neighborNode != prev:
                    subtreeSize = traverseTree(neighborNode, current)
                    if subtreeSize == 0:
                        isUniform = False
                    else:
                        if colors[neighborNode] == colors[current]:
                            totalSameColor += subtreeSize
                        else:
                            isUniform = False

                processNeighbor(idx + 1)

            processNeighbor(0)

            if isUniform:
                if maxSize < totalSameColor:
                    maxSize = totalSameColor
                return totalSameColor
            else:
                return 0

        return traverseTree(0, -1)