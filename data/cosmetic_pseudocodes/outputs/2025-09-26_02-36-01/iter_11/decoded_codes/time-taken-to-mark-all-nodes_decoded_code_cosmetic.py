from collections import deque
from typing import List

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        size = len(edges) + 1
        adjacencyMap = self.buildGraph(edges, size)

        def bfs(origin: int) -> int:
            processingQueue = deque()
            processingQueue.append((origin, 0))
            visitFlags = [False] * size
            visitFlags[origin] = True
            ceilingTime = 0

            while processingQueue:
                node, clk = processingQueue.popleft()
                if ceilingTime < clk:
                    ceilingTime = clk
                for neighborNode in adjacencyMap[node]:
                    if not visitFlags[neighborNode]:
                        visitFlags[neighborNode] = True
                        if neighborNode % 2 == 0:
                            processingQueue.append((neighborNode, clk + 2))
                        else:
                            processingQueue.append((neighborNode, clk + 1))
            return ceilingTime

        def buildGraph(edgeList: List[List[int]], size: int) -> List[List[int]]:
            mapObj = [[] for _ in range(size)]
            def auxFillGraph(idx: int) -> List[List[int]]:
                if idx >= len(edgeList):
                    return mapObj
                u, v = edgeList[idx]
                mapObj[u].append(v)
                mapObj[v].append(u)
                return auxFillGraph(idx + 1)
            return auxFillGraph(0)

        resultTimes = [0] * size
        counter = 0
        while counter < size:
            resultTimes[counter] = bfs(counter)
            counter += 1

        return resultTimes