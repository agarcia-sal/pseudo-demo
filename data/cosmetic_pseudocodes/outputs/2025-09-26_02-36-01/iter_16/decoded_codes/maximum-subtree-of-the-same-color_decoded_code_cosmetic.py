from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        nodesToNeighbors = defaultdict(list)
        for firstElement, secondElement in edges:
            nodesToNeighbors[firstElement].append(secondElement)
            nodesToNeighbors[secondElement].append(firstElement)

        result = 1

        def dfs(currentNode: int, parentNode: int) -> int:
            nonlocal result
            colorGroupCount = 1
            flagAllChildrenMatch = True

            for neighborNode in nodesToNeighbors[currentNode]:
                if neighborNode != parentNode:
                    subtreeCount = dfs(neighborNode, currentNode)
                    if subtreeCount == 0:
                        flagAllChildrenMatch = False
                    else:
                        if colors[neighborNode] == colors[currentNode]:
                            colorGroupCount += subtreeCount
                        else:
                            flagAllChildrenMatch = False

            if flagAllChildrenMatch:
                result = max(result, colorGroupCount)
                return colorGroupCount
            else:
                return 0

        dfs(0, -1)
        return result