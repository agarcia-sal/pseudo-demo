from collections import deque

class Solution:
    def timeTaken(self, edges):
        countNodes = len(edges) + 1
        adjacency = [[] for _ in range(countNodes)]
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        def bfs(origin):
            dq = deque()
            dq.append((origin, 0))
            visitedFlags = [False] * countNodes
            visitedFlags[origin] = True
            maximumDuration = 0

            def processQueue():
                nonlocal maximumDuration
                if not dq:
                    return
                currentNode, currentTime = dq.popleft()
                if maximumDuration < currentTime:
                    maximumDuration = currentTime

                neighborsList = adjacency[currentNode]
                position = 0

                def handleNeighbors(pos):
                    if pos == len(neighborsList):
                        return
                    neighborNode = neighborsList[pos]
                    if not visitedFlags[neighborNode]:
                        visitedFlags[neighborNode] = True
                        timeIncrement = 2 if (neighborNode % 2 == 0) else 1
                        dq.append((neighborNode, currentTime + timeIncrement))
                    handleNeighbors(pos + 1)

                handleNeighbors(position)
                processQueue()

            processQueue()
            return maximumDuration

        resultsArray = []
        idx = 0

        def iterateIndices():
            nonlocal idx
            if idx == countNodes:
                return
            tempResult = bfs(idx)
            resultsArray.append(tempResult)
            idx += 1
            iterateIndices()

        iterateIndices()
        return resultsArray