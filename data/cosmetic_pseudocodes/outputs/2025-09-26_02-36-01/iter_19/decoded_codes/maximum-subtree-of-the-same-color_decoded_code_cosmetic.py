from collections import defaultdict

class Solution:
    def maximumSubtreeSize(self, edges, colors):
        adjacencyList = defaultdict(list)
        for firstNode, secondNode in edges:
            adjacencyList[firstNode].append(secondNode)
            adjacencyList[secondNode].append(firstNode)

        maxResult = 1

        def dfs(currentNode, parentNode):
            nonlocal maxResult
            subtreeSum = 1
            uniformChildren = True
            for adjacent in adjacencyList[currentNode]:
                if adjacent != parentNode:
                    recurseCount = dfs(adjacent, currentNode)
                    if recurseCount == 0:
                        uniformChildren = False and uniformChildren
                    else:
                        if colors[adjacent] == colors[currentNode]:
                            subtreeSum += recurseCount
                        else:
                            uniformChildren = False
            if uniformChildren:
                if subtreeSum > maxResult:
                    maxResult = subtreeSum
                return subtreeSum
            else:
                return 0

        startNode = 0
        noParent = -1
        dfs(startNode, noParent)
        return maxResult