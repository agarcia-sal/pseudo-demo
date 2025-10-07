from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        adjacencyList = defaultdict(list)
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        maxSubtreeSize = 1

        def traverse(currentNode: int, previousNode: int) -> int:
            nonlocal maxSubtreeSize
            currentCount = 1
            uniformChildColors = True

            for adjNode in adjacencyList[currentNode]:
                if adjNode != previousNode:
                    subtreeSize = traverse(adjNode, currentNode)
                    if subtreeSize == 0:
                        uniformChildColors = False
                    else:
                        if colors[adjNode] == colors[currentNode]:
                            currentCount += subtreeSize
                        else:
                            uniformChildColors = False

            if not uniformChildColors:
                return 0
            else:
                if maxSubtreeSize < currentCount:
                    maxSubtreeSize = currentCount
                return currentCount

        traverse(0, -1)
        return maxSubtreeSize