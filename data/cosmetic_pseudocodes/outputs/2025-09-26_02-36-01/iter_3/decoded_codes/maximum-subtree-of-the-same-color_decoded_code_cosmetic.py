from collections import defaultdict

class Solution:
    def maximumSubtreeSize(self, edges, colors):
        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        bestSize = 1

        def dfs(currentNode, parentNode):
            nonlocal bestSize
            identicalCount = 1
            allKidsMatch = True
            for adjNode in adjacency[currentNode]:
                if adjNode != parentNode:
                    subSize = dfs(adjNode, currentNode)
                    if subSize == 0:
                        allKidsMatch = False
                    else:
                        if colors[adjNode] == colors[currentNode]:
                            identicalCount += subSize
                        else:
                            allKidsMatch = False
            if allKidsMatch:
                if identicalCount > bestSize:
                    bestSize = identicalCount
                return identicalCount
            else:
                return 0

        dfs(0, -1)
        return bestSize