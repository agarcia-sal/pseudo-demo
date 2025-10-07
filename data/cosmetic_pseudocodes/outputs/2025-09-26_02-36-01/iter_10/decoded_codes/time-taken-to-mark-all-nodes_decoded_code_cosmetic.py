from collections import deque, defaultdict

class Solution:
    def timeTaken(self, edges):
        totalNodes = len(edges) + 1
        adjacencyMap = self.build_adj_map(edges)

        def bfs(root):
            queueContainer = deque([(root, 0)])
            visitationFlags = [False] * totalNodes
            visitationFlags[root] = True
            peakTime = 0
            while queueContainer:
                nodeAtFront, timeAtFront = queueContainer.popleft()
                if peakTime < timeAtFront:
                    peakTime = timeAtFront
                for childNode in adjacencyMap[nodeAtFront]:
                    if not visitationFlags[childNode]:
                        visitationFlags[childNode] = True
                        if childNode % 2 == 0:
                            queueContainer.append((childNode, timeAtFront + 2))
                        else:
                            queueContainer.append((childNode, timeAtFront + 1))
            return peakTime

        def build_adj_map(edgeList):
            mapAdjacency = defaultdict(list)
            for startNode, endNode in edgeList:
                mapAdjacency[startNode].append(endNode)
                mapAdjacency[endNode].append(startNode)
            # Ensure all nodes are keys in the adjacency map
            for node in range(totalNodes):
                mapAdjacency.setdefault(node, [])
            return mapAdjacency

        accumTimes = [0] * totalNodes

        def fill_times(currentIndex):
            if currentIndex >= totalNodes:
                return
            accumTimes[currentIndex] = bfs(currentIndex)
            fill_times(currentIndex + 1)

        fill_times(0)
        return accumTimes