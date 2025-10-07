from collections import deque
from typing import List

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        totalVertices = len(edges) + 1

        # Build adjacency list
        adjacencyMap = [[] for _ in range(totalVertices)]
        for u, v in edges:
            adjacencyMap[u].append(v)
            adjacencyMap[v].append(u)

        def bfs(startNode: int) -> int:
            deq = deque([(startNode, 0)])
            visitedFlags = [False] * totalVertices
            visitedFlags[startNode] = True
            currentMax = 0

            while deq:
                nodeVal, elapsed = deq.popleft()
                if currentMax < elapsed:
                    currentMax = elapsed

                for adjacentNode in adjacencyMap[nodeVal]:
                    if not visitedFlags[adjacentNode]:
                        visitedFlags[adjacentNode] = True
                        if adjacentNode % 2 == 0:
                            deq.append((adjacentNode, elapsed + 2))
                        else:
                            deq.append((adjacentNode, elapsed + 1))

            return currentMax

        resultTimes = [0] * totalVertices
        idx = 0
        while idx < totalVertices:
            resultTimes[idx] = bfs(idx)
            idx += 1

        return resultTimes