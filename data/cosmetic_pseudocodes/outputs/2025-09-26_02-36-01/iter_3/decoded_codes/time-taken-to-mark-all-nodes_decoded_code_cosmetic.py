from collections import deque
from typing import List, Dict

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        totalNodes = len(edges) + 1
        adjacencyMap: Dict[int, List[int]] = {i: [] for i in range(totalNodes)}
        for u, v in edges:
            adjacencyMap[u].append(v)
            adjacencyMap[v].append(u)

        def bfs(origin: int) -> int:
            dequeStructure = deque([(origin, 0)])
            visitedFlags = [False] * totalNodes
            visitedFlags[origin] = True
            greatestDuration = 0

            while dequeStructure:
                currentNode, elapse = dequeStructure.popleft()
                if greatestDuration < elapse:
                    greatestDuration = elapse

                for neighbor in adjacencyMap[currentNode]:
                    if not visitedFlags[neighbor]:
                        visitedFlags[neighbor] = True
                        delay = 2 if (neighbor % 2) == 0 else 1
                        dequeStructure.append((neighbor, elapse + delay))

            return greatestDuration

        durations = [0] * totalNodes
        for pos in range(totalNodes):
            durations[pos] = bfs(pos)

        return durations