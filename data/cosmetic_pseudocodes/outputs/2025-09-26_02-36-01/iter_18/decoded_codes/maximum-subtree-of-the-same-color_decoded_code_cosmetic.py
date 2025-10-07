from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        neighborMap = defaultdict(list)
        indexA = 0
        while indexA < len(edges):
            pairX = edges[indexA]
            firstNode, secondNode = pairX[0], pairX[1]
            neighborMap[firstNode].append(secondNode)
            neighborMap[secondNode].append(firstNode)
            indexA += 1

        maxSubtreeCount = 1

        def dfs(currentNode: int, ancestorNode: int) -> int:
            nonlocal maxSubtreeCount
            colorGroupCount = 1
            isUniformChildren = True
            locIter = 0
            neighbors = neighborMap[currentNode]

            while locIter < len(neighbors):
                adjNode = neighbors[locIter]
                if adjNode != ancestorNode:
                    subtreeSize = dfs(adjNode, currentNode)
                    if subtreeSize == 0:
                        isUniformChildren = False
                    else:
                        if colors[adjNode] == colors[currentNode]:
                            colorGroupCount += subtreeSize
                        else:
                            isUniformChildren = False
                locIter += 1

            if isUniformChildren:
                if maxSubtreeCount < colorGroupCount:
                    maxSubtreeCount = colorGroupCount
                return colorGroupCount
            else:
                return 0

        startNode = 0
        invalidNode = -1
        _ = dfs(startNode, invalidNode)
        return maxSubtreeCount