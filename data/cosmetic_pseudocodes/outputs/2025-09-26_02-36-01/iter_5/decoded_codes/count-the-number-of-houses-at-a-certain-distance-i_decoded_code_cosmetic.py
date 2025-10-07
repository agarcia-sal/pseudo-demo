from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        counts = [0] * n

        def bfs(origin: int) -> None:
            visitedFlags = [False] * (n + 1)
            distToNodes = [0] * (n + 1)
            nodesToVisit = deque([origin])
            visitedFlags[origin] = True

            def processNeighbors(currentNode: int) -> None:
                if 1 <= currentNode <= n:
                    for adjacentNode in (currentNode - 1, currentNode + 1):
                        if 1 <= adjacentNode <= n and not visitedFlags[adjacentNode]:
                            visitedFlags[adjacentNode] = True
                            distToNodes[adjacentNode] = distToNodes[currentNode] + 1
                            nodesToVisit.append(adjacentNode)

            def bfsRecursion() -> None:
                if not nodesToVisit:
                    return
                currNode = nodesToVisit.popleft()
                processNeighbors(currNode)
                if currNode == x and not visitedFlags[y]:
                    visitedFlags[y] = True
                    distToNodes[y] = distToNodes[currNode] + 1
                    nodesToVisit.append(y)
                if currNode == y and not visitedFlags[x]:
                    visitedFlags[x] = True
                    distToNodes[x] = distToNodes[currNode] + 1
                    nodesToVisit.append(x)
                bfsRecursion()

            bfsRecursion()

            for idx in range(1, n + 1):
                if distToNodes[idx] > 0:
                    counts[distToNodes[idx] - 1] += 1

        for counter in range(1, n + 1):
            bfs(counter)

        return counts