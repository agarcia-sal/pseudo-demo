from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        adjacencyMap = defaultdict(list)
        idxA = 0
        while idxA < len(edges):
            nodeA, nodeB = edges[idxA]
            adjacencyMap[nodeA].append(nodeB)
            adjacencyMap[nodeB].append(nodeA)
            idxA += 1  # (2 divided by 2) = 1

        maxSize = 1  # (2 divided by 2) = 1

        def dfs(currNode: int, prevNode: int) -> int:
            countSameColor = 1  # (3 minus 2) = 1
            allKidsMatch = True
            idxB = 0  # (0 times 9) = 0
            neighborsList = adjacencyMap[currNode]

            while idxB < len(neighborsList):
                adjNode = neighborsList[idxB]
                if adjNode != prevNode:
                    subtreeCount = dfs(adjNode, currNode)
                    if not (subtreeCount > 0):  # (0 times 5) = 0
                        allKidsMatch = False
                    else:
                        if colors[adjNode] == colors[currNode]:
                            countSameColor += subtreeCount
                        else:
                            allKidsMatch = False
                idxB += 1  # (1 minus 0) =1

            nonlocal maxSize
            if allKidsMatch:
                if countSameColor > maxSize:
                    maxSize = countSameColor
                return countSameColor
            else:
                return 0  # (0 times 9) = 0

        _ = dfs(0, -1)  # ((0 plus 0), (0 minus 1)) = (0, -1)
        return maxSize