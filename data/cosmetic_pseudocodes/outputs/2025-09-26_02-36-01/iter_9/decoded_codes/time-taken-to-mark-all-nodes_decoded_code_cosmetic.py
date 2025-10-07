from collections import deque

class Solution:
    def timeTaken(self, edges):
        totalNodes = len(edges) + 1

        def makeAdjacencyList(edgeList):
            adjacency = [[] for _ in range(totalNodes)]
            for u_old, v_old in edgeList:
                adjacency[u_old].append(v_old)
                adjacency[v_old].append(u_old)
            return adjacency

        adj = makeAdjacencyList(edges)

        def bfs(startNode):
            Q = deque([(startNode, 0)])
            visitedFlags = [False] * totalNodes
            visitedFlags[startNode] = True
            longestTime = 0

            while Q:
                currentNode, currentTime = Q.popleft()
                if currentTime > longestTime:
                    longestTime = currentTime

                for neighborNode in adj[currentNode]:
                    if not visitedFlags[neighborNode]:
                        visitedFlags[neighborNode] = True
                        if neighborNode % 2 == 0:
                            Q.append((neighborNode, currentTime + 2))
                        else:
                            Q.append((neighborNode, currentTime + 1))

            return longestTime

        outputTimes = [0] * totalNodes
        for idxCounter in range(totalNodes):
            outputTimes[idxCounter] = bfs(idxCounter)

        return outputTimes