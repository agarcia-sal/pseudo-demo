from collections import deque, defaultdict

class Solution:
    def timeTaken(self, edges):
        countVertices = len(edges) + 1

        adjacencyMap = defaultdict(list)
        for u, v in edges:
            adjacencyMap[u].append(v)
            adjacencyMap[v].append(u)

        def traverseBFS(origin):
            elementsQueue = deque([(origin, 0)])
            visitedFlags = [False] * countVertices
            visitedFlags[origin] = True
            greatestDuration = 0

            while elementsQueue:
                nodeCurrent, durationCurrent = elementsQueue.popleft()
                if greatestDuration < durationCurrent:
                    greatestDuration = durationCurrent

                for adjNode in adjacencyMap[nodeCurrent]:
                    if not visitedFlags[adjNode]:
                        visitedFlags[adjNode] = True
                        if adjNode % 2 == 0:
                            elementsQueue.append((adjNode, durationCurrent + 2))
                        else:
                            elementsQueue.append((adjNode, durationCurrent + 1))

            return greatestDuration

        durations = []
        for indexIter in range(countVertices):
            durations.append(traverseBFS(indexIter))

        return durations