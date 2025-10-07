from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maximumSubtreeSize(self, edges: List[Tuple[int, int]], colors: List[int]) -> int:
        adjacencyMap = defaultdict(list)
        for firstNode, secondNode in edges:
            adjacencyMap[firstNode].append(secondNode)
            adjacencyMap[secondNode].append(firstNode)

        maxSize = 1

        def dfs(currNode: int, prevNode: int) -> int:
            nonlocal maxSize
            countSameColorSubtree = 1
            isUniformColorChildren = True
            for neighborNode in adjacencyMap[currNode]:
                if neighborNode != prevNode:
                    subtreeSize = dfs(neighborNode, currNode)
                    if subtreeSize == 0:
                        isUniformColorChildren = False
                    elif colors[neighborNode] == colors[currNode]:
                        countSameColorSubtree += subtreeSize
                    else:
                        isUniformColorChildren = False
            if isUniformColorChildren:
                if maxSize < countSameColorSubtree:
                    maxSize = countSameColorSubtree
                return countSameColorSubtree
            else:
                return 0

        dfs(0, -1)
        return maxSize