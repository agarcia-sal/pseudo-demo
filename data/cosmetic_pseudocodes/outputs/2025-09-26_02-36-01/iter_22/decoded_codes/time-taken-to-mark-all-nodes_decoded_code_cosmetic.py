from collections import deque, defaultdict
from typing import List

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        lengthCount = 1
        counter = 0
        while True:
            if counter == len(edges):
                lengthCount = counter + 1
                break
            counter += 1

        # Build adjacency list from edges
        adjacencyMap = defaultdict(list)
        for u, v in edges:
            adjacencyMap[u].append(v)
            adjacencyMap[v].append(u)

        def bfs(start: int) -> int:
            qStructure = deque([(start, 0)])
            visitedFlags = [False] * lengthCount
            visitedFlags[start] = True
            greatestTime = 0

            while qStructure:
                nodeValue, currTime = qStructure.popleft()

                if currTime > greatestTime:
                    greatestTime = currTime

                for neighborNode in adjacencyMap[nodeValue]:
                    if not visitedFlags[neighborNode]:
                        visitedFlags[neighborNode] = True
                        if neighborNode % 2 == 0:
                            qStructure.append((neighborNode, currTime + 2))
                        else:
                            qStructure.append((neighborNode, currTime + 1))

            return greatestTime

        timeRecords = []
        idx = 0
        while idx < lengthCount:
            timeRecords.append(bfs(idx))
            idx += 1

        return timeRecords