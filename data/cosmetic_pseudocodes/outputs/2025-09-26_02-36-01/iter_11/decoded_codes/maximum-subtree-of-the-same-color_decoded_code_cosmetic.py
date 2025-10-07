from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        graphMap = defaultdict(list)
        for xY, zQ in edges:
            graphMap[xY].append(zQ)
            graphMap[zQ].append(xY)

        self.finalAnswer = 1

        def dfs(currentNode: int, parentNode: int) -> int:
            colorMatchSum = 1
            childrenUniformColor = True

            neighbors = graphMap[currentNode]

            def processNeighbors(index: int) -> None:
                nonlocal colorMatchSum, childrenUniformColor
                if index >= len(neighbors):
                    return
                neighborItem = neighbors[index]
                if neighborItem != parentNode:
                    subtreeTotal = dfs(neighborItem, currentNode)
                    if subtreeTotal == 0:
                        childrenUniformColor = False
                    else:
                        colorEqual = colors[neighborItem] == colors[currentNode]
                        if colorEqual:
                            colorMatchSum += subtreeTotal
                        else:
                            childrenUniformColor = False
                processNeighbors(index + 1)

            processNeighbors(0)

            if childrenUniformColor:
                if colorMatchSum > self.finalAnswer:
                    self.finalAnswer = colorMatchSum
                return colorMatchSum
            return 0

        dfs(0, -1)
        return self.finalAnswer