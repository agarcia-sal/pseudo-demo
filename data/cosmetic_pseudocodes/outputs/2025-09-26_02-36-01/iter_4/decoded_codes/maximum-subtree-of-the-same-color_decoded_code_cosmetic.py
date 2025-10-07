from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        adjacency = defaultdict(list)
        for firstNode, secondNode in edges:
            adjacency[firstNode].append(secondNode)
            adjacency[secondNode].append(firstNode)

        maxResult = 1

        def dfs(currentNode: int, parentNode: int) -> int:
            nonlocal maxResult
            countOfSameColor = 1
            allChildMatch = True
            for adjNode in adjacency[currentNode]:
                if adjNode != parentNode:
                    subtreeSize = dfs(adjNode, currentNode)
                    if subtreeSize == 0:
                        allChildMatch = False
                    else:
                        if colors[adjNode] == colors[currentNode]:
                            countOfSameColor += subtreeSize
                        else:
                            allChildMatch = False
            if allChildMatch:
                if maxResult < countOfSameColor:
                    maxResult = countOfSameColor
                return countOfSameColor
            else:
                return 0

        dfs(0, -1)
        return maxResult