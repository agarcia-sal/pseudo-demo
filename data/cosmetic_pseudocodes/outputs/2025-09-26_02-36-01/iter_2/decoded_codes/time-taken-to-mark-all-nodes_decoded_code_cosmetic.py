from collections import deque
from typing import List

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        totalNodes = len(edges) + 1

        # Construct adjacency list from edges
        adjacency = [[] for _ in range(totalNodes)]
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        def bfs(source: int) -> int:
            visitedFlags = [False] * totalNodes
            visitedFlags[source] = True
            processingQueue = deque([(source, 0)])
            longestDuration = 0

            while processingQueue:
                currentNode, currentTime = processingQueue.popleft()
                if longestDuration < currentTime:
                    longestDuration = currentTime

                for adjNode in adjacency[currentNode]:
                    if not visitedFlags[adjNode]:
                        visitedFlags[adjNode] = True
                        if adjNode % 2 == 0:
                            processingQueue.append((adjNode, currentTime + 2))
                        else:
                            processingQueue.append((adjNode, currentTime + 1))

            return longestDuration

        collectedTimes = [0] * totalNodes
        position = 0
        while position < totalNodes:
            collectedTimes[position] = bfs(position)
            position += 1

        return collectedTimes